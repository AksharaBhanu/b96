import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#write a code to select & deselect all options in reverse order
driver = Chrome()
driver.get("file:///F:/B96%20Selenium/workspace/pages/Sample12.html")
time.sleep(2)
listbox=driver.find_element(By.ID,"A3")
select=Select(listbox)

a=select.first_selected_option
print(a.text) #lunch
print("*"*10)

b=select.all_selected_options
for c in b:
    print(c.text)  #L S D

print("*"*10)
d=select.options
for e in d:
    print(e.text)  #B L S D

