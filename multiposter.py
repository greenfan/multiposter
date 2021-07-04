#!/usr/bin/python
import feedparser
from doingit_d import diaspora
from mastodon import mastodon
import sys
import time
from datetime import datetime

# file for output
logfile = open('logoutput.txt', 'a')

errlog = open('erroutput.txt', 'a')



print("=======Today's date is: {}=======\n".format(datetime.today()), file = logfile)
# Begin scraping RSS feed
#url = "https://zapier.com/engine/rss/8954721/solarstuff2"
url = "http://www.newsblur.com/reader/starred_rss/605591/89d85fb786d7/tech"
NewsFeed = feedparser.parse(url)

# If multiposter.py was run with arguments, check them
argcount = len(sys.argv)
print("argcount is {}".format(argcount), file = logfile)

# Determine how many articles we're posting
if argcount == 2:
    postcount = int(sys.argv[1])
else:
    todays_date = format(datetime.today().day).zfill(2)
    postcount = 0
    for i in range(0, 7):
        # DECALRE entry
        entry = NewsFeed.entries[i]
        pdate = entry.published.split()
        # Add time divergence
        if todays_date in pdate[1]:
            postcount = postcount + 1
        print(entry.title, file = logfile)
        print(entry.link, file = logfile)

print(f"Postcount is {postcount}, printing {postcount} entires. . . ")

if __name__=="__main__":
    try:
        mastodon()
        print("Completed posting to Mastodon successfully", file = logfile)
    except:
        pass
        print("Mastodon did not work out trying next", file = errlog)

    try:
        diaspora()
        print("Completed posting to Diaspora successfully", file = logfile)
    except:
        pass
        print("Diaspora did not work out trying next", file = errlog)

logfile.close()

errlog.close()
