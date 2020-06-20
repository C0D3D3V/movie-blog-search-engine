#!/usr/bin/env python

"""
Inspired form https://github.com/sydev/movie-blog-api
"""


import re
import sys
import json
import html
import xmltodict
import urllib.parse

try:
    # In unix readline needs to be loaded so that
    # arrowkeys work in input
    import readline  # noqa: F401
except ImportError:
    pass

from pyquery import PyQuery as pq
from http.client import HTTPSConnection

stdHeader = {
    'User-Agent': ('Mozilla/5.0 (X11; Linux x86_64)' +
                   ' AppleWebKit/537.36 (KHTML, like Gecko)' +
                   ' Chrome/78.0.3904.108 Safari/537.36'),
    'Content-Type': 'application/x-www-form-urlencoded'
}

connection = HTTPSConnection('movie-blog.sx')

speed_units = ['kb/s', 'kbps', 'mb/s',
               'mbps', 'Kbp', 'VIDEO', '@', 'Video', 'Größe']

relevant_providers = ['Zippyshare.com', 'anonfile.com']


class Movie_Blog_Entry:

    def __init__(self, title: str, link: str, speed_information: [],
                 link_list: []):
        self.title = title
        self.link = link
        self.speed_information = speed_information
        self.link_list = link_list

    def __str__(self):

        output = ""

        output += "\n# {}".format(self.title)
        output += "\n# {}".format(self.link)
        if(len(self.speed_information) > 0):
            output += "\n# {}".format(self.speed_information)

        for link in self.link_list:
            output += "\n{}".format(link)

        return output


def convert_xml_to_dict(xml: str):
    """
    Converts a xml string to a dictionary
    """
    xml_dict = xmltodict.parse(xml)
    json_str = json.dumps(xml_dict)
    converted_dict = json.loads(json_str)
    return converted_dict


def get_speed_information(html_content: str):
    speed_information = []
    html_lines = re.sub(r'<\s*br\s*(/)?>', '\n', html_content)
    html_lines = html_lines.split('\n')
    for line in html_lines:
        cleaned_line = html.unescape(line)
        cleaned_line = re.sub("<.*?>", " ", cleaned_line)
        cleaned_line = ' '.join(cleaned_line.split())
        for unit in speed_units:
            if cleaned_line.find(unit) >= 0:
                speed_information.append(cleaned_line)
                break

    return speed_information


def search(query='') -> [Movie_Blog_Entry]:
    q = urllib.parse.quote(query)
    url = '/?s={}&feed=rss2'.format(q)

    try:
        connection.request(
            'GET',
            url,
            headers=stdHeader
        )
        response = connection.getresponse()
        xml = response.read()

        page_dict = convert_xml_to_dict(xml)

        page_rss_dict = page_dict.get('rss', {})
        page_items = page_rss_dict.get('channel', {}).get('item', [])

        # entries are mapped to there provider
        mapped_entries = {}

        for item in page_items:
            item_content = item.get('content:encoded', '')
            item_title = item.get('title', '')
            item_link = item.get('link', '')

            speed_information = get_speed_information(item_content)

            d = pq(item_content)
            links = d('span[id^=mirror][style] a')

            mapped_links = {}

            for provider in relevant_providers:
                for link in links:
                    if link.text == provider:
                        link_href = link.attrib.get('href', '')
                        if(link_href != ''):
                            if (provider not in mapped_links):
                                mapped_links[provider] = []

                            mapped_links[provider].append(link_href)

            for provider in mapped_links:
                if (provider not in mapped_entries):
                    mapped_entries[provider] = []

                new_entry = Movie_Blog_Entry(
                    item_title, item_link, speed_information,
                    mapped_links[provider])

                mapped_entries[provider].append(new_entry)

        return mapped_entries

    except Exception as e:
        print(e)

    return {}


def print_entries(mapped_entries: {}):

    if(len(mapped_entries) == 0):
        print('No links found!')

    for provider in mapped_entries:
        entries_list = mapped_entries[provider]

        print('\n\n{}\n'.format(provider))
        for entry in entries_list:
            print(entry)


if(len(sys.argv) > 1):
    q = ' '.join(sys.argv[1:])
    print_entries(search(q))
    readline.add_history(q)


while True:
    print('\n\n\n')
    print('#'*60)
    print('\n\n\n')
    search_input = input('Search for:   ')
    print_entries(search(search_input))
