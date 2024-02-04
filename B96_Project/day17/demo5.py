import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

driver = Chrome()
#WebDriverWait(browser,timeout,poll_frequecy)
wait=WebDriverWait(driver,10,1)
driver.get("file:///F:/B96%20Selenium/workspace/pages/Sample13.html")
driver.find_element(By.ID,"ok").click()
wait.until(EC.alert_is_present())
alert=driver.switch_to.alert
print(alert.text)
alert.accept()
