from __main__ import *

from datetime import datetime
from selenium import webdriver
import sys
import time
import re
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Configure our webdriver


options = webdriver.ChromeOptions()
#options.add_argument('headless');
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome(options=options)

# End web browser config
def minds():
    
    driver.get('https://www.minds.com/newsfeed/subscriptions')

    time.sleep(10)
    from multiposter import postcount
    from multiposter import NewsFeed
    print(postcount)

    username = driver.find_element_by_css_selector("#username")

    password = driver.find_element_by_css_selector("#password")
    username.send_keys("Horton")
    time.sleep(2)
    username.send_keys(Keys.TAB)
    time.sleep(2.5)
    password.send_keys("hortonhearsawho")
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/m-app/m-page/m-body/div/div/m-login/div/div/div/minds-form-login/form/div[2]/m-shadowboxsubmitbutton/button/div").click()
    username = driver.find_element_by_css_selector("#username")
    print("Okay done")
    time.sleep(4)





### Begin action

    for i in reversed(range(0, postcount)):
        entry = NewsFeed.entries[i]
        pdate = entry.published
        driver.find_element_by_xpath(
            "/html/body/m-app/m-page/m-body/div/div/m-newsfeed/div/div[1]/m-newsfeed--subscribed/m-composer/div").click()
        time.sleep(2)


        #    textbox = driver.find_element_by_xpath("/html/body/m-app/m-page/m-overlay-modal/div[2]/m-composer__modal/m-composer__base/div/div/m-composer__textarea/div/m-text-input--autocomplete-container/textarea")

        textbox = driver.find_element_by_xpath("/html/body/m-app/m-page/m-overlay-modal/div[2]/m-composer__modal/m-composer__base/div/div/div/m-composer__textarea/div/m-text-input--autocomplete-container/textarea")
        print("Found element.")
        textbox.send_keys('{0}'.format((entry.title)))

        #get hash tags
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

        textbox.send_keys(' \n \n \n {0}'.format((entry.summary)))
        textbox.send_keys(' \n {0} \n'.format(entry.link))
        time.sleep(3)

        textbox.send_keys(' \n {0}'.format( ', '.join(fullhash[:5])))


        driver.find_element_by_xpath("/html/body/m-app/m-page/m-overlay-modal/div[2]/m-composer__modal/m-composer__base/div/div/m-composer__toolbar/div/m-button/a").click()
        time.sleep(5)
        driver.get('https://www.duck.com')
        time.sleep(5)
        driver.get('https://www.minds.com/newsfeed/subscriptions')
        time.sleep(360)


