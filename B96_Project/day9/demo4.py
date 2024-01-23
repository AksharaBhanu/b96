import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("file:///F:/B96%20Selenium/workspace/pages/sample7.html")
time.sleep(2)
# driver.find_element(By.ID,"A8").click()
# time.sleep(2)
driver.find_element(By.ID,"A8").submit()
time.sleep(2)
