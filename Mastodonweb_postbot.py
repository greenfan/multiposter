from selenium import webdriver 
from selenium.webdriver.common.action_chains import ActionChains

import feedparser
import sys
import time
from datetime import datetime
#from selenium import webdriver
from bs4 import BeautifulSoup
import re
import random
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


#### T_Count

def tab_selektor(n):
 #   nn = 0
    for _ in range(n):
        
        elem.send_keys(Keys.TAB)
        time.sleep(1)
#        print(f"tabbing {nn}")
#        nn = nn + 1

todays_date = format(datetime.today().day).zfill(2)


argcount = len(sys.argv)

print(todays_date)

####

if argcount >= 2:
    postcount = int(sys.argv[1])
else:
    postcount = 0
    for i in range(0, 10):
        # DECALRE entry
        entry = NewsFeed.entries[i]
        pdate = entry.published.split('T')[0]
        pdate = str(pdate)[5:]
        if todays_date in pdate:
            t_count = t_count + 1





























# Navigate to mastodon

driver.get("https://mastodon.online/auth/sign_in")
driver.implicitly_wait(5) # Waits up to 5 seconds for elements to appear

# LOGIN
time.sleep(3)
action = ActionChains(driver)
action.move_by_offset(538, 375).click().perform()
time.sleep(2.5)
elem = driver.switch_to.active_element
elem.send_keys("opensciencedaily@a2security.net")
time.sleep(1.5)
elem.send_keys(Keys.TAB)
elem = driver.switch_to.active_element
time.sleep(0.5)
elem.send_keys("password!")
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
    print("No stupid found")
    pass
    



print("ABOUT TO POST.")
driver.implicitly_wait(5)

script = "return [window.scrollX + arguments[0], window.scrollY + arguments[1]];"

mouse_coords = driver.execute_script(script, 0, 0)
print(f"Mouse is at {mouse_coords}")


for i in reversed(range(postcount)):
    try:

        entry = NewsFeed.entries[i]
        print(f"""posting {entry.title} 
        """)
        time.sleep(3)
        elem = driver.switch_to.active_element
        tab_selektor(7)
        time.sleep(.35)
        
        
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
            nice_summary = ( nice_summary[:175] + "..." )if len(nice_summary) > 176 else nice_summary
        except:
            soup = BeautifulSoup(entry.summary, features="html.parser")
            nice_summary = soup.get_text()
            nice_summary = ( nice_summary[:170] + "..." )if len(nice_summary) > 171 else nice_summary
        
        
        
        
        elem.send_keys(f"""{entry.title}
           
Article Source: {entry.link}
        
{nice_summary}
""")
        elem.send_keys(' \n {0}'.format(', '.join(fullhash[:5])))
        

        tab_selektor(7)
    
        elem.send_keys(Keys.ENTER)
    except Exception:
        print("there was an exception")
    
    time.sleep(335)
    driver.get("https://mastodon.online/home")
    driver.implicitly_wait(5)
    
    
    
    
