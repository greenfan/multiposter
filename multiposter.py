#!/usr/bin/python
import feedparser
from doingit_d import diaspora
from mastodon import mastodon
from doingit_minds import minds
import sys
import time
from datetime import datetime

#url = "https://zapier.com/engine/rss/7955983/OpenScienceRSS"
url = "https://zapier.com/engine/rss/8203027/sciencefeed"
NewsFeed = feedparser.parse(url)


argcount = len(sys.argv)
print("argcount is {}".format(argcount))

if argcount == 2:
    postcount = int(sys.argv[1])
else:
    todays_date = format(datetime.today().day).zfill(2)
    postcount = 0
    for i in range(0, 10):
        # DECALRE entry
        entry = NewsFeed.entries[i]
        pdate = entry.published.split()
        # Add time divergence
        if todays_date in pdate[1]:
            postcount = postcount + 1
        print(entry.title)
print(postcount)


if __name__=="__main__":
#    minds()
#    mastodon()
    diaspora()

