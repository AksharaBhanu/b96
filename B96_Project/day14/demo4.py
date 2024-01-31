import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("file:///F:/B96%20Selenium/workspace/pages/sample3.html")
time.sleep(2)
# e=driver.find_element(By.TAG_NAME,"b")
# print(type(e)) #WebElement

all_links=driver.find_elements(By.TAG_NAME,"a")
for link in all_links:
    print(link.get_attribute('href'))