#import required libraries
import urllib2, urllib #used for url call
from urllib2 import urlopen #used for url check
import requests #used for html requests
from bs4 import BeautifulSoup #used for html scrap
from lxml import html #used for processing html
import json #return format
import sys
import argparse #argument parser


def web_scrap(maxRec_):
    URL = 'https://news.ycombinator.com/'
    main_url = URL
    page = requests.get(main_url)
    soup = BeautifulSoup(page.text, 'lxml')
    #html parser

    maxRec = maxRec_
    records = [] 
    #array of dictionaries

    cnt=0 #count for the records array

    #link, title and rank are under tag tr
    for div in soup.find_all('tr', class_="athing"):
        a = div.find_all('a', class_="storylink", ) #uri and title are under tag a class athing

        #Below is for URL Validation but it does not work, 403 Forbidden
        #ret = urllib2.urlopen(a[0].get("href"))
        #if ret.code == 200: uri = a[0].get("href")

        uri = a[0].get("href") #returns uri value for the current loop which is in a[0]
        title = a[0].text #returns title value for the current loop which is in a[0] as a text
        span = div.find_all('span', class_="rank", ) #rank is under tag span class rank
        rank, s = span[0].text.split('.') #split with dot to get rank as a number

        #check for negative number as a point value
        if (rank < 0): rank = 0
        else: rank, s = span[0].text.split('.')

        records.append({"title": title, "uri":uri, "rank": rank}) #add pairs to the current index of array of dictionaries
        cnt = cnt + 1 #increase count for iteration through records array
        if cnt==maxRec: break

    cnt = 0 #decrease count to zero to add pairs 

    #points author and comments are under tag td class subtext
    for div in soup.find_all('td', class_="subtext"):
        a = div.find_all('a') #find all a tags in the td tag of the current loop

        #check for empty author value
        if (a[0].text): author = a[0].text #returns author value for the current loop which is in a[0]
        else:  author = 'no author name'
        comments_arr = a[3].text.split() #returns author value for the current loop which is in a[0], split to remove string 'comment'

        #check for non-number or negative number value appearing as a comment value
        if comments_arr[0] == 'discuss' or comments_arr[0] < 0 :comments = '0'
        else:comments = comments_arr[0] #comments_arr[0]=number of comments

        span = div.find_all('span') #points is under span tag
        points_arr = span[0].text.split()

        #check for negative number as a point value
        if (points_arr[0] < 0): points = 0
        else: points = points_arr[0]


        #update dictionary with new pairs
        records[cnt].update({'points': points}) 
        records[cnt].update({'author': author})
        records[cnt].update({'comments': comments})
        cnt = cnt+1 #increase count for iteration through records array
        if cnt==maxRec: break


    #Dict to JSON conversion
    python2json=json.dumps(records, indent=4)
    print python2json

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--posts", help="how many posts to print. A positive integer <= 100")
    args = parser.parse_args()
    if args.posts:
    	if 0 < int(args.posts) <= 100:
    		web_scrap(int(args.posts))
    	else:
    		print "Posts must be a positive integer <= 100"
    else:
    	parser.print_help()
		
