from __main__ import *
from datetime import datetime
from selenium import webdriver
import sys
import time
import re
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
# Configure our web browser



options = webdriver.ChromeOptions()
options.add_argument('headless');
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
#options.binary_location = "/usr/bin/chromium"
options.add_argument('window-size=1920x1480')
driver = webdriver.Chrome(options=options)

# End web browser config
def mastodon():
    driver.get('https://mastodon.online/web/timelines/home')

    from multiposter import postcount
    from multiposter import NewsFeed
    print(f"I am mastodon, posting {postcount} entires...")



#login
    username = driver.find_element_by_id("user_email")
    password = driver.find_element_by_id("user_password")
    username.send_keys("opensciencedaily@a2security.net")
    time.sleep(2)
    username.send_keys(Keys.TAB)
    time.sleep(2.5)
    password.send_keys("HelloThere!!")
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/form/div[3]/button").click()

# begin posting


    textbox = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[1]/div/div/div[3]/div[2]/div[1]/label/textarea")
    print("Found element.")
    time.sleep(3)
    for i in reversed(range(0, postcount)):
        entry = NewsFeed.entries[i]
        pdate = entry.published

        #    textbox = driver.find_element_by_xpath("/html/body/m-app/m-page/m-overlay-modal/div[2]/m-composer__modal/m-composer__base/div/div/m-composer__textarea/div/m-text-input--autocomplete-container/textarea")

        textbox.send_keys('{0}'.format((entry.title)))

        # get hash tags
        try:
            hashtags = entry.author
            hashtags2 = re.sub("[ ]", ",", hashtags)
            hashlist = re.split(',', hashtags2)
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

        art_summary = ( entry.summary[:90] + '...' ) if len(entry.summary) > 93 else entry.summary

        textbox.send_keys(' \n \n \n {0}'.format((art_summary)))
        textbox.send_keys(' \n {0} \n'.format(entry.link))
        print("Posting entry: {}".format(entry.title))
        time.sleep(3)

        textbox.send_keys(' \n {0}'.format(', '.join(fullhash[:8])))



        driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[1]/div/div/div[3]/div[5]/div/button").click()
        time.sleep(300)


