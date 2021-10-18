#!/usr/bin/python
import feedparser
import sys
import time
from datetime import datetime
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
# Configure our web browser



options = webdriver.ChromeOptions()
#
#
#options.add_argument('headless');
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
options.add_argument('window-size=1920x1480')
driver = webdriver.Chrome(options=options)
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
    time_var = 369



print(f"\n\n\nPosting {t_count} in {time_var} variable increments.")

"""
if __name__=="__main__":
    try:
        #mastodon()
        print("hello")
    except:
        pass
        print("Mastodon did not work out trying next")

    try:
        diaspora()
    except:
        pass
        print("Diaspora did not work out trying next")
"""



def mastodon():
    driver.get('https://mastodon.online/web/timelines/home')

#login
    username = driver.find_element_by_id("user_email")
    password = driver.find_element_by_id("user_password")
    username.send_keys("opensciencedaily@a2security.net")
    time.sleep(2)
    username.send_keys(Keys.TAB)
    time.sleep(2.5)
    password.send_keys("Zxcvfgfg21*&")
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/form/div[3]/button").click()
# begin posting

    textbox = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[1]/div/div/div[3]/div[2]/div[1]/label/textarea")
    print("Found element.")



    for i in reversed(range(0, t_count)):




        print("attempting parse")
        entry = NewsFeed.entries[i]



        textbox.send_keys('{0}'.format((entry.title)))

        # get hash tag
        try:
            hashtags = [t.term for t in entry.tags]
            hashtags2 = ' '.join(map(str, hashtags))
            hashlist = re.split(' ', hashtags2)
            hashlist = hashlist[0:9]
            hashlistnum = len(hashlist)

        except AttributeError:
            itemlist = ["solar", "energy", "news", "renewable", "PV", "hydrogen", "sustainability",
                        "photovoltaic", "green", "technology", "science"]
            hashlist = random.choices(itemlist, k=6)

        hash = ['#' + i for i in hashlist]

        # REmove unwanted hashtags
        stop_words = ["#&", "#and", "#a", "#", "#with", "#the", "#for", "#company", "#of"]
        # Finally declare hashtags as fullhash
        fullhash = list(set(filter(lambda w: w not in stop_words, hash)))
                # get article summary with beautifulsoup
        try:
            soup = BeautifulSoup(entry.summary, features="html.parser")
            nice_summary = soup.find('p').get_text()
            nice_summary = ( nice_summary[:70] + "..." )if len(nice_summary) > 90 else nice_summary
        except:
            soup = BeautifulSoup(entry.summary, features="html.parser")
            nice_summary = soup.get_text()
            nice_summary = ( nice_summary[:70] + "..." )if len(nice_summary) > 90 else nice_summary


        textbox.send_keys(' \n \n \n{0}'.format((nice_summary)))
        textbox.send_keys(' \nArticle Source: {0} \n'.format(entry.link))
        time.sleep(3)

        textbox.send_keys(' \n {0}'.format(', '.join(fullhash[:8])))



        driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[1]/div/div/div[3]/div[5]/div/button").click()
        time.sleep(time_var)
        
        
mastodon()



def diaspora():

    print(type(time_var))
    print(time_var)

    for i in reversed(range(0, t_count)):

        entry = NewsFeed.entries[i]
        # Configure our web browser
        options = webdriver.ChromeOptions()
       # options.add_argument('headless');
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--test-type")
    #    options.binary_location = "/usr/bin/chromium"
        options.add_argument('window-size=2120x1280')
        driver = webdriver.Chrome(options=options)
        # End web browser config

        driver.get('https://diasp.org/stream')

        time.sleep(3)

        ### Begin Actions
        username = driver.find_element_by_css_selector("#user_username")
        password = driver.find_element_by_css_selector("#user_password")
        username.send_keys("opensciencedaily" + Keys.TAB)
        password.send_keys("Zxcvfgfg21" + Keys.ENTER)


        driver.get('https://diasp.org/stream')
        time.sleep(15)
        textbox = driver.find_element_by_css_selector("#status_message_text")


        pdate = entry.published
        textbox.send_keys('#### {0}\n****\n'.format((entry.title)))
        time.sleep(0.5)

       # try:
        try:
            hashtags = [t.term for t in entry.tags]
            hashtags2 = ' '.join(map(str, hashtags))
            hashlist = re.split(' ', hashtags2)
            hashlist = hashlist[0:9]
            hashlistnum = len(hashlist)


        except AttributeError:
            itemlist = ["solar", "energy", "news", "renewable", "PV", "hydrogen", "solarpower", "sustainability",
                        "photovoltaic", "green", "renewableenergy", "futurology", "RSS"]
            hashlist = random.choices(itemlist, k=5)

        hash = ['#' + i for i in hashlist]

        # REmove unwanted hashtags
        stop_words = ["#&", "#and", "#a", "#", "#with", "#the", "#for", "#company", "#of"]
        # Finally declare hashtags as fullhash
        fullhash = list(set(filter(lambda w: w not in stop_words, hash)))
        print(*fullhash)
                # get article summary with beautifulsoup
        try:
            soup = BeautifulSoup(entry.summary, features="html.parser")
            nice_summary = soup.find('p').get_text()
        except:
            soup = BeautifulSoup(entry.summary, features="html.parser")
            nice_summary = soup.get_text()
# end article summary

        textbox.send_keys('> {0}\n {1} \n {2} \n ****'.format(nice_summary, entry.link, ', '.join(fullhash)))
        time.sleep(1)
        submitbutton = driver.find_element_by_css_selector("#submit").click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="submit"]').click()

        time.sleep(time_var)

        driver.close()

diaspora()

