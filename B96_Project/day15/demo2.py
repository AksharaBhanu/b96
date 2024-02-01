import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = Chrome()
driver.get("file:///F:/B96%20Selenium/workspace/pages/Sample11.html")
time.sleep(2)
listbox=driver.find_element(By.ID,"A1")
select=Select(listbox)
#print the content of the listbox
alloptions=select.options
count=len(alloptions)
print('Number of options in listbox is',count)

for option in alloptions:
    print(option.text)
