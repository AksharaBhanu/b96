import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#check if Delhi is present in the listbox or not (searhing)
expected="Tumkur"
driver = Chrome()
driver.get("file:///F:/B96%20Selenium/workspace/pages/Sample11.html")
time.sleep(2)
listbox=driver.find_element(By.ID,"A1")
select=Select(listbox)
count=0
for option in select.options:
    if option.text==expected:
        count+=1

if count==0:
    print(expected,' is not present')
elif count==1:
    print(expected, ' is present -Not duplicate')
else:
    print(expected, ' is present ',count,' times and it is duplicate')