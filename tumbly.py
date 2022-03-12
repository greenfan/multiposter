#!/bin/shebang
# tumbly.py v3

# extending multiposter to post to tumblr

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



# file for output
todays_date = format(datetime.today().day).zfill(2)
# Begin scraping RSS feed
url = "http://www.newsblur.com/reader/starred_rss/605591/89d85fb786d7/tech"
NewsFeed = feedparser.parse(url)
# If multiposter.py was run with arguments, check them

driver = webdriver.Firefox()




driver.set_window_size(860, 1080)

todays_date = format(datetime.today().day).zfill(2)
print(todays_date)



argcount = len(sys.argv)
print(f"Stories to post:\n\n\n")
time.sleep(1)
print(f"fetching data")


for i in range (10):
    print(". ", end=' ')
    time.sleep(.03)
    print(".")

for i in range (10):
    print(". ", end=' ')
    time.sleep(.031)
    print(".")
    print(". ", end=' ')
    time.sleep(.031)

print(".")
time.sleep(1)
if argcount >= 2:
    t_count = int(sys.argv[1])
else:
    t_count = 0
    for i in range(0, 10):
        # DECALRE entry
        entry = NewsFeed.entries[i]
        pdate = entry.published.split('T')[0]
        pdate = str(pdate)[5:]
        if todays_date in pdate:
            t_count = t_count + 1

for i in range(0, t_count):
    entry = NewsFeed.entries[i]
    print(f"{entry.title}\n")
    time.sleep(.3)

if argcount == 3:
    time_var = int(sys.argv[2])
else:
    time_var = 969



print(f"\n\n\nPosting {t_count} in {time_var} variable increments.")




def tumbly():
    for i in reversed(range(0, t_count)):

        driver.get('https://www.tumblr.com/login')


        usernamebox = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/div/section/div/form/div[1]/input")

        passbox = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/div/section/div/form/div[2]/input")
        usernamebox.send_keys("futurepowered@a2security.net")
        time.sleep(1)
        passbox.send_keys("")
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/div/section/div/form/button/span").click()
        time.sleep(10)
        print("Successfully logged in...")
        time.sleep(16)



        driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/header/div[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div/div/div[4]/div/div[2]/div/nav/div/nav/ul[1]/li[1]/a/span").click()
        time.sleep(10)






        pdate = entry.published
        print('#### {0}\n****\n'.format((entry.title)))



        elem = driver.switch_to.active_element

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

        elem.send_keys("{0} \n {1}".format(nice_summary, entry.link))


        a = ActionChains(driver)
        a.key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT).send_keys('{0}'.format(entry.title))
        a.perform()



        driver.find_element_by_xpath("/html/body/div/div/div[4]/div/div/div/div/div[2]/div/div[2]/div/span/span/textarea")


        bwc ="#".join(fullhash)
        driver.find_element_by_xpath("/html/body/div/div/div[4]/div/div/div/div/div[2]/div/div[2]/div/span/span/textarea").send_keys('{0}'.format(bwc))

        elem = driver.switch_to.active_element


        driver.find_element_by_xpath("/html/body/div/div/div[4]/div/div/div/div/div[1]/div[1]/div/div/button").click()


tumbly()
print("found elements")
time.sleep(10)





