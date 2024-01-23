import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("file:///F:/B96%20Selenium/workspace/pages/sample2.html")
time.sleep(2)

tag=driver.find_element(By.ID,"a1").tag_name
print(tag)

attribute_value=driver.find_element(By.ID,"a1").get_attribute('href')
print(attribute_value)

attribute_value=driver.find_element(By.ID,"a1").get_attribute('title')
print(attribute_value)

text=driver.find_element(By.ID,"a1").text
print(text)

outer_html=driver.find_element(By.ID,"a1").get_property('outerHTML')
print(outer_html)