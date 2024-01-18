import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
driver=Chrome()
driver.get("file:///F:/B96%20Selenium/pages/sample2.html")
time.sleep(2)
element=driver.find_element(By.TAG_NAME,"x")
element.click()
time.sleep(4)
