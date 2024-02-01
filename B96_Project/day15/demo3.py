import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#check if Delhi is present in the listbox or not (searhing)
expected="Agra"
msg='Not Present'
driver = Chrome()
driver.get("file:///F:/B96%20Selenium/workspace/pages/Sample11.html")
time.sleep(2)
listbox=driver.find_element(By.ID,"A1")
select=Select(listbox)
for option in select.options:
    text=option.text
    if text==expected:
        msg=' is present'
        break

print(expected,msg)