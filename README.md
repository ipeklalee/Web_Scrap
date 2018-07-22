# About
Web_Scrap is a python script that does data extraction from the URL=https://news.ycombinator.com/news?p=2
Application takes max number of records to return as a parameter, outputs to STDOUT in JSON Format.
It extracts "title", "uri", "author", "points", "comment", "rank" values for top posts in the web site.

# Usage
python hackernews.py --posts n
python hackernews.py: calls the program n: how many posts to print. A positive integer <= 100.
