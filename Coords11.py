from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

import feedparser
import sys
import time
from datetime import datetime
from bs4 import BeautifulSoup
import re
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

# Initialize the Firefox WebDriver




# Set up Firefox options
firefox_options = Options()
firefox_options.add_argument("--width=1280")  # Specify width
firefox_options.add_argument("--height=920")  # Specify height

# Initialize the Firefox WebDriver with options
driver = webdriver.Firefox(options=firefox_options)

# Begin polling NewsBlur RSS feed
#todays_date = format(datetime.today().day).zfill(2)
# Begin scraping RSS feed
url = "http://www.newsblur.com/reader/starred_rss/605591/89d85fb786d7/tech"
NewsFeed = feedparser.parse(url)

################################
#### FUNCTIONS START

def tab_selektor(n):
    for _ in range(n):

        elem.send_keys(Keys.TAB)
        time.sleep(1)



def generate_hash(article_concat, salty_keywords):
    cleaned_summary = article_concat.lower()
    hashtags = [keyword for keyword in salty_keywords if keyword in cleaned_summary]
    return hashtags

def remove_duplicates(words):
    return list(set(words))

##### FUNCTIONS END
###
#


todays_date = format(datetime.today().day).zfill(2)
argcount = len(sys.argv)
####

if argcount >= 2:
    postcount = int(sys.argv[1])
else:
    postcount = 0
    t_count = 0
    for i in range(0, 10):
        # DECALRE entry
        entry = NewsFeed.entries[i]
        pdate = entry.published.split('T')[0]
        pdate = str(pdate)[5:]
        if todays_date in pdate:
            t_count = t_count + 1
        postcount = t_count

print(f"posting {postcount} stories today")
# Navigate to mastodon








####                      ####
#### Driver begin actions ####
###
###







driver.get("https://mastodon.online/auth/sign_in")
driver.implicitly_wait(5) # Waits up to 5 seconds for elements to appear

# LOGIN
time.sleep(3)
action = ActionChains(driver)
action.move_by_offset(538, 375).click().perform()
time.sleep(2.5)
elem = driver.switch_to.active_element
elem.send_keys("opensciencedaily")
time.sleep(1.5)
elem.send_keys(Keys.TAB)
elem = driver.switch_to.active_element
time.sleep(0.5)
elem.send_keys("XXX")
time.sleep(1.5)
elem = driver.switch_to.active_element
elem.send_keys(Keys.ENTER)


## check for resend page

try:
    time.sleep(2)
    print("Checking if button exists")
    button = driver.find_element_by_xpath("/html/body/div/div[3]/form/div[2]/button")
    print("Button exists", button_element.text)



    element_1 = driver.find_element_by_id=("user_email")


    time.sleep(2.5)
    element_1.send_keys("opensciencedaily@a2security.net")
    time.sleep(.5)
    element_1.send_keys(Keys.ENTER)


except Exception:
    print("No email redirect occurred")
    pass




for i in reversed(range(postcount)):
    try:


        print("ABOUT TO POST.")
        driver.implicitly_wait(5)

        script = "return [window.scrollX + arguments[0], window.scrollY + arguments[1]];"

        mouse_coords = driver.execute_script(script, 0, 0)


        print(f"Clicked..... Mouse is at {mouse_coords}")

        elem = driver.switch_to.active_element
        #elem = driver.switch_to.active_element
        print("tabbing 5 times")

        elem = driver.switch_to.active_element
        tab_selektor(5)
        print("we should be active on the post box")


        elem = driver.switch_to.active_element





        entry = NewsFeed.entries[i]
        print(f"""posting {entry.title}
        """)
        time.sleep(3)
        tab_selektor(5)
        textbox = driver.switch_to.active_element
        time.sleep(.35)

            # get article summary with beautifulsoup
        try:
            soup = BeautifulSoup(entry.summary, features="html.parser")
            article_summary = soup.find('p').get_text()
            print(f"Printing article summary.... {article_summary}")
            time.sleep(9)
            nice_summary = ( article_summary[:175] + "..." )if len(article_summary) > 176 else article_summary
        except:
            soup = BeautifulSoup(entry.summary, features="html.parser")
            article_summary = soup.get_text()
            nice_summary = ( article_summary[:170] + "..." )if len(article_summary) > 171 else article_summary

        fullhash = ""
        hashlist = ""

        ######################## keyword section START

        try:
            hashtags = [t.term for t in entry.tags]
            hashtags2 = ' '.join(map(str, hashtags))
            hashlist = re.split(' ', hashtags2)
            hashlist = hashlist[0:9]
            hashlistnum = len(hashlist)

        except AttributeError:
            entry.tags = [""]
            hashlist = ["electricity", "renewable"]
            pass


        #### if no keywords exist in RSS feed do the following to generate list of keywords based on entry summary and title
        #generate summary
        article_concat = article_summary + entry.title
        print(f"the content is.... {article_concat}...")


# add all states
        salty_keywords = ["solar", "electric", "kentucky", "tennessee", "electricity", "japanese", "japan", "wind", "legislation", "robots", "robotics", "energy", "manufacturing", "usa",  "power", "energy", "news", "renewable", "pv", "hydrogen", "sustainability", "photovoltaic", "space", "microreactor", "reactor", "storage",  "green", "technology", "science", "maine", "florida", "offshore", "nasa", "spacex", "research", "weather", "nuclear", "fusion", "fission", "tesla", "wyoming", "brazil"]

        new_hash = generate_hash(article_concat, salty_keywords)

        hashlist = new_hash + hashlist


        #remove duplicates
        hashlist = remove_duplicates(hashlist)


        hashlist = ['#' + i for i in hashlist]

        # Remove unwanted hashtags
        stop_words = ["#&", "#markets", "#projects", "#and", "#a", "#", "#it", "#with", "#the", "#for", "#company", "#of", "#components", "news", "#modules", "#sponsored", "#featured" ]
        # Finally declare hashtags as fullhash
        fullhash = list(set(filter(lambda w: w not in stop_words, hashlist)))

        #remove later
        print(f" full list of tags: {fullhash}")
        ######################## improved keyword  section END
        #changing behavior to just post output for now

        elem.send_keys(f"""{entry.title}

Article Source: {entry.link}

{nice_summary}
""")
        elem.send_keys(' \n {0}'.format(' '.join(fullhash[:5])))
        #time.sleep(4)
        elem.send_keys(Keys.Enter)
        time.sleep(1)
        elem.send_keys(Keys.Enter)
        elem = driver.switch_to.active_element
        time.sleep(1)
        elem.send_keys(Keys.Enter)
        print("tabbing, then hitting enter...")
        time.sleep(1)
        elem = driver.switch_to.active_element
        tab_selektor(7)
        time.sleep(1)
        elem.send_keys(Keys.ENTER)
        print("tabbing again, then hitting enter... I am seriously trying hard")
        elem = driver.switch_to.active_element
        print("switched to active element")
        elem.send_keys(Keys.ENTER)
        elem.send_keys(Keys.TAB)
        print("tab...")
        elem.send_keys(Keys.TAB)
        print("tab...")
        elem.send_keys(Keys.TAB)
        print("tab...")
        elem.send_keys(Keys.TAB)
        print("tab...")
        elem.send_keys(Keys.TAB)
        print("tab...")
        elem.send_keys(Keys.TAB)
        print("tab...")
        elem.send_keys(Keys.TAB)
        print("tab...")
        #tab_selektor(7)
        time.sleep(1)
        elem.send_keys(Keys.ENTER)


    except Exception:
        print("there was an exception doing tabbing")

        print(f"""{entry.title}

Article Source: {entry.link}

{nice_summary}
{fullhash}
""")

        elem.send_keys(Keys.ENTER)
        elem.send_keys(Keys.TAB)
        print("tab...")

        elem.send_keys(Keys.TAB)
        print("tab...")
        elem.send_keys(Keys.TAB)
        print("tab...")
        elem.send_keys(Keys.TAB)
        print("tab...")
        elem.send_keys(Keys.TAB)
        print("tab...")
        elem.send_keys(Keys.TAB)
        print("tab...")
        elem.send_keys(Keys.TAB)
        print("tab...")
        #tab_selektor(7)
        time.sleep(1)
        elem.send_keys(Keys.ENTER)
        elem = driver.switch_to.active_element



        elem.send_keys(Keys.TAB)



        bbutton = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div/div/form/div[2]/div[2]/div[2]/div[2]/button")
        bbutton.click()
        print("Clicked latest link...")
        time.sleep(1)
        print("hitting enter now....")
        elem.send_keys(Keys.ENTER)
        print("Hit enter.")
        print("We POSTED IT!!! sleeping 3 then reloading page")
        time.sleep(3)
        driver.get("https://mastodon.online/home")

    time.sleep(6)

    driver.get("https://mastodon.online/home")
    driver.implicitly_wait(5)
