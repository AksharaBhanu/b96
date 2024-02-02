import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = Chrome()
driver.get("file:///F:/B96%20Selenium/workspace/pages/Sample13.html")
driver.find_element(By.ID,"ok").click()
time.sleep(4)
alert=driver.switch_to.alert
print(alert.text)
alert.accept()