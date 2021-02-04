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

for i in range(0,count4today()):
    # DECALRE entry
    entry = NewsFeed.entries[i]
    try:
        ttags = [t.term for t in entry.tags]
    except:
        ttags = "no tags for this one"
    print(entry.title)
    print(ttags)
    print(entry.link)


# get article summary with beautifulsoup
    try:
        soup = BeautifulSoup(entry.summary, features="html.parser")
        page = soup.find('p').get_text()
        print(page)
    except:
        soup = BeautifulSoup(entry.summary, features="html.parser")
        print(soup.get_text())
# end article summary
