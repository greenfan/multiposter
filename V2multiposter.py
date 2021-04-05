#!/usr/bin/python
from doingit_d import diaspora
from mastodon import mastodon
from bs4 import BeautifulSoup
import feedparser
from datetime import datetime,timedelta
import os
import sys

# file for output
logfile = open('logoutput.txt', 'a')
errlog = open('erroutput.txt', 'a')

print("=======Today's date is: {}=======\n".format(datetime.today()), file = logfile)

# Begin scraping RSS feed
url = "https://www.newsblur.com/reader/starred_rss/605591/89d85fb786d7/tech"
NewsFeed = feedparser.parse(url)
total_stories = len(NewsFeed)

date_today = format(datetime.today().day).zfill(2) + "-" + format(datetime.today().month).zfill(2)
print(date_today)




def count4today():
    t_c = 0
    for i in range(0,8):
        entry = NewsFeed.entries[i]
        s = entry.published
        pdate = datetime.strptime(s,"%Y-%m-%dT%H:%M:%SZ")
        pubdate = str(pdate)
        print(pubdate)
        fdate = pubdate[5:10]
        print(fdate)
        if date_today in str(fdate):
            t_c = t_c + 1
    return(t_c)

if len(sys.argv) != 2:
    count2post = count4today()
else:
    count2post = sys.argv[1]
print(f"count 2 post is {count2post}")

#count2post = count4today()
print(f"count to post is {count2post}")
dattempt = 0
try:
    if dattempt == 0:
        diaspora()
        print("Completed posting to Diaspora successfully", file = logfile)
        print("completed diaspora")
        dattempt = 1
    else:
        pass
except:
    pass
    print("Diaspora did not work out trying next", file = logfile)
try:
    mastodon()
    print("Completed posting to Mastodon successfully", file = logfile)
    print("completed Mastodon")
    print(f"da attempt is {daattempt}")
    print("attempting to stop this beast.")
    logfile.close()
    os.system('''kill -9 $( ps faux | grep -i v2 | awk ' { print $2 } ')''')
    os.system(" kill -9 $( ps faux | grep v2 | awk '{print  $2 }' ) ")

except:
    print("something fucked up", file = logfile)
    pass
print("all methods finished correctly, if this prints, something odd is going on stuck in a loop")
os.system("kill -9 $( ps faux | grep v2 | awk '{print  $2 }' ) ")
logfile.close()

errlog.close()
exit()
