# About
Web_Scrap is a python script that does data extraction from [Hacker News](https://news.ycombinator.com/news?p=2) website. <br/>
Application takes max number of records to return as a parameter, outputs to STDOUT in JSON Format. <br/>
It extracts "title", "uri", "author", "points", "comment", "rank" values for top posts in the web site. <br/>

_LIBRARIES:_ <br/>
1- [urllib2, urllib](https://docs.python.org/3/library/urllib.html) - used for opening and reading the URL <br/>
2- [requests](http://docs.python-requests.org/en/master/)  - used for sending HTTP request <br/>
3- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - used for data extraction from the given URL <br/>
4- [lxml](https://lxml.de/)  - used for processing html <br/>
5- [json](https://docs.python.org/2/library/json.html) - required for return format <br/>
6- [sys](https://docs.python.org/2/library/sys.html) - used to interact with the command line <br/>
7- [argparse](https://docs.python.org/2/library/argparse.html) - used to parse arguments <br/>

# Usage
Python Python 2.7.10 is required to run this application. [install Python 2.7.10 ](https://www.python.org/downloads/release/python-2710/") <br/>
CMD call: python hackernews.py --posts n <br/>
Description: python hackernews.py: calls the program n: how many posts to print. A positive integer <= 100.
