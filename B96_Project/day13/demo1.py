import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
print(id(driver))
driver.get("file:///F:/B96%20Selenium/workspace/pages/Sample10.html")
cwh=driver.current_window_handle
print(cwh)
