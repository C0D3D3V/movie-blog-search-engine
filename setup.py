from os import path
from setuptools import setup


def readme():
    this_directory = path.abspath(path.dirname(__file__))
    with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        return f.read()


setup(
    name='movie-blog-search-engine',
    version='0.5',
    description='Search on movie-blog for download links',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/C0D3D3V/movie-blog-search-engine/',
    author='C0D3D3V',
    license='GPL-3.0',
    scripts=['movie'],
    python_requires='>=3',
    install_requires=[
        'xmltodict',
        'pyquery',
        'requests',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Communications :: File Sharing',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Multimedia :: Video',
    ],
    zip_safe=False,
)
