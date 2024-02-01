import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#print the content of the listbox in sorted order
driver = Chrome()
driver.get("file:///F:/B96%20Selenium/workspace/pages/Sample12.html")
time.sleep(2)
listbox=driver.find_element(By.ID,"A2")
select=Select(listbox)

all_options=[]
for option in select.options:
    all_options.append(option.text)

print(all_options)
all_options.sort()
print(all_options)

#home work: reverse Z-A order
#check if the content of the listbox is already sorted or not