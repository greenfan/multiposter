#!/usr/bin/python
import feedparser
#from doingit_d import diaspora
#from mastodon import mastodon
import sys
import time
from datetime import datetime
# file for output
todays_date = format(datetime.today().day).zfill(2)
# Begin scraping RSS feed
url = "http://www.newsblur.com/reader/starred_rss/605591/89d85fb786d7/tech"
NewsFeed = feedparser.parse(url)
# If multiposter.py was run with arguments, check them


todays_date = format(datetime.today().day).zfill(2)



argcount = len(sys.argv)
print(f"today's day number is {todays_date}")

if argcount >= 2:
    t_count = int(sys.argv[1])
else:
    t_count = 0

    print("T count {}".format(t_count))
    # Count manually to find out how many ### to post  t_count === number of stories to post
    for i in range(0, 10):
        # DECALRE entry
        entry = NewsFeed.entries[i]
        pdate = entry.published.split('T')[0]
        print(pdate)
        # Add time divergence
        if todays_date in pdate:
            t_count = t_count + 1
        print(entry.title)


if argcount == 3:
    time_var = int(sys.argv[2])
else:
    time_var = int(369)
    
    

print(f"posting {t_count} in {time_var} variable increments.")
