import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
driver = Chrome()
driver.get("https://aksharatraining.com/")
time.sleep(3)

driver.execute_script("window.scrollBy(0,3000)")
time.sleep(3)
driver.execute_script("window.scrollTo(0,500)") #scroll to top
time.sleep(4)
#write a script to scroll to Join the revolution!