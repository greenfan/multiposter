from bs4 import BeautifulSoup
import requests
import feedparser
import cgi
from datetime import datetime,timedelta

# file for output
logfile = open('logoutput.txt', 'a')
errlog = open('erroutput.txt', 'a')

print("=======Today's date is: {}=======\n".format(datetime.today()), file = logfile)

# Begin scraping RSS feed
url = "https://www.newsblur.com/reader/starred_rss/605591/89d85fb786d7/tech"
NewsFeed = feedparser.parse(url)


date_today = format(datetime.today().day).zfill(2)
print(date_today)

for i in range(0,7):
    # DECALRE entry
    entry = NewsFeed.entries[i]
    try:
        ttags = [t.term for t in entry.tags]
    except:
        ttags = "no tags for this one"
    print(entry.title)
    print(ttags)
    print(entry.link)
    try:
        soup = BeautifulSoup(entry.summary, features="html.parser")
        page = soup.find('p').get_text()
        print(page)
    except:
        print(entry.summary)
       #pass
    s = entry.published
    pdate = datetime.strptime(s,"%Y-%m-%dT%H:%M:%SZ")
    print(format(pdate.day).zfill(2))
    print('\n')

