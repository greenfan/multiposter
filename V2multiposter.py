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


# get article summary with beautifulsoup
    try:
        soup = BeautifulSoup(entry.summary, features="html.parser")
        page = soup.find('p').get_text()
        print(page)
    except:
        soup = BeautifulSoup(entry.summary, features="html.parser")
        print(soup.get_text())
# end article summary



# get date for today's entrys
#    3s = entry.published
#    pdate = datetime.strptime(s,"%Y-%m-%dT%H:%M:%SZ")
#    print(format(pdate.day).zfill(2))
#    print('\n')
# end date



date_today = format(datetime.today().day).zfill(2)
'''
for i in range(0, total_stories):
    entry = NewsFeed.entries[1]
    s = entry.published

    pdate = datetime.strptime(s,"%Y-%m-%dT%H:%M:%SZ")
    if date_today in str(pdate):
        t_c = t_c + 1
    print(t_c)
'''
def count4today():
    t_c = 0
    for i in range(0, total_stories):
        entry = NewsFeed.entries[1]
        s = entry.published

        pdate = datetime.strptime(s,"%Y-%m-%dT%H:%M:%SZ")
        if date_today in str(pdate):
            t_c = t_c + 1
    return(t_c)
'''
def howmany():
    date_today = format(datetime.today().day).zfill(2)
    print(date_today)
    totalc = 0
    print(total_stories)
    for i in range(0,total_stories):
        entry = NewsFeed.entries[i]
        s = entry.published
        pdate = datetime.strptime(s,"%Y-%m-%dT%H:%M:%SZ")
        print(pdate)
        if date_today in str(pdate):
            totalc = totalc + 1
            print(totalc)
        print(totalc)
        return totalc

#print(howmany())
howmany()
'''
print(count4today())
