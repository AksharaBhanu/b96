import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
driver = Chrome()
driver.get("file:///F:/B96%20Selenium/workspace/pages/sample7.html")
a=driver.find_element(By.ID,"A1").is_enabled()
print(a) #True--Element is enabled
a=driver.find_element(By.ID,"A4").is_enabled()
print(a) #False--Element is disabled
time.sleep(1)
driver.find_element(By.ID,"A4").send_keys("Akshara")