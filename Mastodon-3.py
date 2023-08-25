from selenium import webdriver 
from selenium.webdriver.common.action_chains import ActionChains

#import feedparser
import sys
import time
#from datetime import datetime
#from selenium import webdriver
#from bs4 import BeautifulSoup
#import re
#import random
#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Initialize the Firefox WebDriver


driver = webdriver.Firefox()


# Navigate to the target page

driver.get("https://book.com")

# Wait for the page to load (replace with your specific condition or more advanced waits) driver.implicitly_wait(5) # Waits up to 5 seconds for elements to appear

# Perform the mouse move and click action using ActionChains 
action = ActionChains(driver)

#Move mouse to the top of the page at coordinates (x=100, y=100) and click
print("success!")
action.move_by_offset(100, 100).click().perform()
time.sleep(1)
action.move_by_offset(140, 140).click().perform()
time.sleep(1)
action.move_by_offset(186, 160).click().perform()
action.move_by_offset(198, 190).click().perform()
action.move_by_offset(200, 200).click().perform()
time.sleep(1)
action.move_by_offset(220, 220).click().perform()

print("success!")
# Optionally, keep the browser window open until you manually close it

# Uncomment the line below to activate

# input("Press Enter to close the browser...")

# Close the browser

driver.quit()
