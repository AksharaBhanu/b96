import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


expected="Tumkur"
driver = Chrome()
driver.get("file:///F:/B96%20Selenium/workspace/pages/Sample11.html")
time.sleep(2)
listbox=driver.find_element(By.ID,"A1")
select=Select(listbox)
alloption=select.all_selected_options
for option in alloption:
    print(option.text)

option=select.first_selected_option
print(option.text)

print(select.is_multiple)

select.deselect_all()
