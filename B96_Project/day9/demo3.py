import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("file:///F:/B96%20Selenium/workspace/pages/sample7.html")
time.sleep(1)
driver.find_element(By.ID,"A1").clear()
time.sleep(1)
driver.find_element(By.ID,"A1").send_keys('Akshara')
time.sleep(1)
driver.find_element(By.ID,"A2").click()
time.sleep(3)