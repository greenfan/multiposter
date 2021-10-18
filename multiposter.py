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
print(f"Stories to post:\n\n\n")
time.sleep(1)
print(f"fetching data")


for i in range (10):
    print(""". """)
    time.sleep(.1)

time.sleep(1)
if argcount >= 2:
    t_count = int(sys.argv[1])
else:
    t_count = 0
    for i in range(0, 10):
        # DECALRE entry
        entry = NewsFeed.entries[i]
        pdate = entry.published.split('T')[0]
        if todays_date in pdate:
            t_count = t_count + 1

for i in range(0, t_count):
    entry = NewsFeed.entries[i]
    print(f"{entry.title}\n")
    time.sleep(.3)

if argcount == 3:
    time_var = int(sys.argv[2])
else:
    time_var = int(369)
