import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
driver = Chrome()
driver.get("https://aksharatraining.com/")
time.sleep(1)
#scroll to the bottom of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)") #scroll to bottom
time.sleep(1)
# driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)") #scroll to top

driver.execute_script("window.scrollTo(0,0)") #scroll to top
time.sleep(4)
#write a script to scroll to Join the revolution!