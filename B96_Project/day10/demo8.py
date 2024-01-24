import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
driver = Chrome()
driver.get("https://aksharatraining.com/")
time.sleep(1)

for i in range(7):
    driver.execute_script("window.scrollBy(0,500)") #scroll down
    time.sleep(1)

for i in range(7):
    driver.execute_script("window.scrollBy(0,-500)") #scroll up
    time.sleep(1)


time.sleep(3)