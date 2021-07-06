#from multiposter import NewsFeed
from datetime import datetime
from selenium import webdriver
import sys
import time
import re
import random
from selenium.webdriver.common.keys import Keys



def diaspora():
    from multiposter import NewsFeed
    # Configure our web browser
    options = webdriver.ChromeOptions()
    options.add_argument('headless');
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
#    options.binary_location = "/usr/bin/chromium"
    driver = webdriver.Chrome(options=options)
    # End web browser config

    driver.get('https://diasp.org/stream')

    time.sleep(3)

    ### Begin Actions
    username = driver.find_element_by_css_selector("#user_username")
    password = driver.find_element_by_css_selector("#user_password")
    username.send_keys("opensciencedaily" + Keys.TAB)
    password.send_keys("hellothere" + Keys.ENTER)
    # password.send_keys(u'\ue007')

    driver.get('https://diasp.org/stream')
    time.sleep(15)
    textbox = driver.find_element_by_css_selector("#status_message_text")
    todays_date = format(datetime.today().day).zfill(2)
    print("today's date is: {}.".format(todays_date))
    ### Begin action

    # Begin parsing the RSS Feed
    #
    # 1. Determine how many stories we will post

    argcount = len(sys.argv)
    print("argcount is {}".format(argcount))

    if argcount == 2:
        t_count = int(sys.argv[1])
    else:
        t_count = 0

        print("T count {}".format(t_count))
        # Count manually to find out how many ### to post  t_count === number of stories to post
        for i in range(0, 10):
            # DECALRE entry
            entry = NewsFeed.entries[i]
            pdate = entry.published.split()
            # Add time divergence
            if todays_date in pdate[1]:
                t_count = t_count + 1
            print(entry.title)

    print("total_new_stories from {} is {}".format(todays_date, t_count))

    for i in reversed(range(0, t_count)):
        # DECALRE entry
        entry = NewsFeed.entries[i]
        pdate = entry.published
        textbox.send_keys('#### {0}\n****\n'.format((entry.title)))
        time.sleep(0.5)

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
        time.sleep(699)

    driver.close()
    print("...")
    time.sleep(1)
    print("I have typed it and clicked submit, Master.")
    print(''' I am now trying to close the function.

    .... please wait....
    ''')
    time.sleep(10)
    return()
