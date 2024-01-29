import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import os

driver = Chrome()
driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.ID,"disha-banner-close").click()
time.sleep(5)
