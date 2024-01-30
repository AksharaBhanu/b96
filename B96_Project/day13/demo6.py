import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

#close all the browsers except parent
driver = Chrome()
driver.get("file:///F:/B96%20Selenium/workspace/pages/Sample10.html")
parent=driver.current_window_handle
driver.find_element(By.ID,"A5").click()
time.sleep(1)
all_whs=driver.window_handles
all_whs.remove(parent)

for w in all_whs:
    driver.switch_to.window(w)
    driver.close()
    time.sleep(1)

time.sleep(3)