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
driver.find_element(By.TAG_NAME,"a").click()
go_back(driver)
driver.find_element(By.ID,"a1").click()
go_back(driver)
driver.find_element(By.NAME,"n1").click()
go_back(driver)
driver.find_element(By.CLASS_NAME,"c1").click()
time.sleep(1)
