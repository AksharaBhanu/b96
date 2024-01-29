import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import os

driver = Chrome()
driver.get("file:///F:/B96%20Selenium/workspace/pages/Sample9.html?")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.ID,"A3").click()
time.sleep(2)
driver.find_element(By.ID,"PageLink_5").click()
time.sleep(2)
driver.find_element(By.ID,"DirectLink_13").click()
time.sleep(2)
# Homework: check if the downloaded file is present in downloads folder or not


