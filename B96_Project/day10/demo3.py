import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
driver = Chrome()
driver.get("file:///F:/B96%20Selenium/workspace/pages/sample7.html")
a=driver.find_element(By.ID,"A5").is_selected()
print(a) #True--Element is enabled
a=driver.find_element(By.ID,"A6").is_selected()
print(a) #False--Element is disabled

a=driver.find_element(By.ID,"A1").is_displayed()
print(a) #True--> element is displayed on the page

a=driver.find_element(By.ID,"A3").is_displayed()
print(a)#False--> element is NOT displayed on the page

driver.find_element(By.ID,"A3").click()