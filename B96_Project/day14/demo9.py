import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
#select all the checkboxes
driver = Chrome()
driver.get("file:///F:/B96%20Selenium/workspace/pages/sample6.html")
driver.maximize_window()
time.sleep(2)
all_checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")

for checkbox in all_checkboxes:
    checkbox.click()
    print(checkbox.is_selected())
    time.sleep(1)

for checkbox in reversed(all_checkboxes):
    checkbox.click()
    time.sleep(1)

#home work: select alternative checkboxes
time.sleep(2)