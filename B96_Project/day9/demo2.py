import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
driver = Chrome()
driver.get("file:///F:/B96%20Selenium/workspace/pages/sample6.html")
driver.maximize_window()
time.sleep(1)

SQL=driver.find_element(By.XPATH,"//td[text()='SQL']")

#find the td which is present to left of the SQL element
slno=driver.find_element(locate_with(By.TAG_NAME,"td").to_left_of(SQL)).text
print('slno of SQL',slno)

cost=driver.find_element(locate_with(By.TAG_NAME,"td").to_right_of(SQL)).text
print('cost of sql',cost)

before=driver.find_element(locate_with(By.TAG_NAME,"td").above(SQL)).text
print('sub before sql',before)

after=driver.find_element(locate_with(By.TAG_NAME,"td").below(SQL)).text
print('sub after sql',after)

which=driver.find_element(locate_with(By.TAG_NAME,"td").near(SQL)).text
print('sub after sql',which)

time.sleep(1)