import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#write a code to select & deselect all options in reverse order
driver = Chrome()
driver.get("file:///F:/B96%20Selenium/workspace/pages/Sample12.html")
time.sleep(2)
listbox=driver.find_element(By.ID,"A2")
select=Select(listbox)
time.sleep(2)
count=len(select.options)
for i in reversed(range(count)):
    select.select_by_index(i)
    print(select.options[i].is_selected())
    time.sleep(1)

for i in reversed(range(count)):
    select.deselect_by_index(i)
    print(select.options[i].is_selected())
    time.sleep(1)

time.sleep(2)