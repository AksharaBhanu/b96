import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = Chrome()
driver.get("file:///F:/B96%20Selenium/workspace/pages/Sample12.html")
time.sleep(2)
listbox=driver.find_element(By.ID,"A3")
select=Select(listbox)
select.deselect_all()
time.sleep(2)

#write a code to select all the options present in listbox
count=len(select.options)
for i in range(count):
    select.select_by_index(i)

time.sleep(2)