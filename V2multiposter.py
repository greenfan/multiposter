#!/usr/bin/python
from doingit_d import diaspora
from mastodon import mastodon

from bs4 import BeautifulSoup
import feedparser
from datetime import datetime,timedelta

# file for output
logfile = open('logoutput.txt', 'a')
errlog = open('erroutput.txt', 'a')

print("=======Today's date is: {}=======\n".format(datetime.today()), file = logfile)

# Begin scraping RSS feed
url = "https://www.newsblur.com/reader/starred_rss/605591/89d85fb786d7/tech"
NewsFeed = feedparser.parse(url)
total_stories = len(NewsFeed)

date_today = format(datetime.today().day).zfill(2)



def count4today():
    t_c = 0
    for i in range(0, total_stories):
        entry = NewsFeed.entries[1]
        s = entry.published

        pdate = datetime.strptime(s,"%Y-%m-%dT%H:%M:%SZ")
        if date_today in str(pdate):
            t_c = t_c + 1
    return(t_c)

count2post = count4today()


if __name__=="__main__":
    try:
        diaspora()
        print("Completed posting to Diaspora successfully", file = logfile)
    except:
        pass
        print("Diaspora did not work out trying next", file = errlog)


logfile.close()

errlog.close()
