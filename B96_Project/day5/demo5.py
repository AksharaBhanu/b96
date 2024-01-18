import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

def go_back(driver):
    time.sleep(1)
    driver.back()
    time.sleep(1)

driver=Chrome()
driver.get("file:///F:/B96%20Selenium/pages/sample2.html")
time.sleep(1)
driver.find_element(By.LINK_TEXT,"Google").click()
go_back(driver)
driver.find_element(By.PARTIAL_LINK_TEXT,"Go").click()
time.sleep(1)