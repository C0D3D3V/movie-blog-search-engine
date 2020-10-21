# Movie-Blog search engine

Search on movie-blog for download links.

The links are filtered by provider, by default only links from Zippyshare.com, megaup.net and anonfile.com are displayed.

## Installation

    pip install movie-blog-search-engine

## Usage

To get all links for a movie, execute the following command in a terminal:

    movie Name of the film

```
usage: movie [-h] [-p PROVIDER] [-c] [query [query ...]]

Movie-Blog Search Engine helps to find the links on movie-block.org from different providers.

positional arguments:
  query                 For an instant search just enter your request as a parameter.

optional arguments:
  -h, --help            show this help message and exit
  -p PROVIDER, --provider PROVIDER
                        With this option you can add several individual providers to the search.
  -c, --clear-providers
                        If you set this option the default provider list will be cleared before the specified
                        providers are added to the list.
```

After a search a new search can be started directly.  Or the program can be closed with [Ctrl+C].

An entry can look as follows:

    # Cool.Series.S12.GERMAN.DUBBED.DL.1080p.BluRay.x264-TMSF
    # https://movie-blog.org/cool-series-s12-german-dubbed-dl-1080p-bluray-x264-tmsf/
    # ['Video : x264 @ 1920 x 960 @ 11.3 Mb/s', 'Audio : German 384 kb/s CBR 6 Chnls / English 2 084 kb/s VBR 6 Chnls /', 'Dauer: 59 min | Format: mkv | Größe: 6049 MB | IMDB: 8.6 | Sample']
    https://filecrypt.cc/Container/AAAAAAAAAA.html
    https://filecrypt.cc/Container/BBBBBBBBBB.html
    https://filecrypt.cc/Container/CCCCCCCCCC.html
