import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import os

driver = Chrome()
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH,"//span[text()='Departure']").click()
time.sleep(2)
date_xpath="//div[text()='February 2024']/../..//p[text()='29']"
driver.find_element(By.XPATH,date_xpath).click()
time.sleep(5)