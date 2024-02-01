import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = Chrome()
driver.get("file:///F:/B96%20Selenium/workspace/pages/Sample11.html")
time.sleep(2)
listbox=driver.find_element(By.ID,"A1")
select=Select(listbox)
select.select_by_index(1) #index starts from 0
time.sleep(1)
select.select_by_value("c")
time.sleep(1)
select.select_by_visible_text("Delhi")
time.sleep(3)
