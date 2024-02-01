import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = Chrome()
driver.get("file:///F:/B96%20Selenium/workspace/pages/Sample12.html")
time.sleep(2)
listbox=driver.find_element(By.ID,"A2")
select=Select(listbox)

select.select_by_index(0)
select.select_by_index(0)
select.select_by_value("b")
select.select_by_visible_text("Snacks")
time.sleep(2)
print(select.is_multiple)
select.deselect_by_index(0)
select.deselect_by_value("b")
select.deselect_by_value("b")
select.deselect_by_visible_text("Snacks")
time.sleep(2)