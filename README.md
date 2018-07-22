# About
Web_Scrap is a python script that does data extraction from the URL=https://news.ycombinator.com/news?p=2
Application takes max number of records to return as a parameter, outputs to STDOUT in JSON Format.
It extracts "title", "uri", "author", "points", "comment", "rank" values for top posts in the web site.

Libraries used:
urllib2, urllib - used for opening and reading the URL
requests  - used for sending HTTP request
BeautifulSoup - used for data extraction from the given URL
lxml  - used for processing html
json - required for return format
sys - used to interact with the command line

# Usage
Python Python 2.7.10 is required to run this application. [install Python 2.7.10 ](https://www.python.org/downloads/release/python-2710/")
python hackernews.py --posts n
python hackernews.py: calls the program n: how many posts to print. A positive integer <= 100.
