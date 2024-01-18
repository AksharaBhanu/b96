import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
driver=Chrome()
driver.get("file:///F:/B96%20Selenium/pages/sample3.html")
time.sleep(2)
element=driver.find_element(By.TAG_NAME,"a")
element.click()
time.sleep(4)
