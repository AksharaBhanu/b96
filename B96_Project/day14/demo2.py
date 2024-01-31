import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("file:///F:/B96%20Selenium/workspace/pages/Sample7.html")
time.sleep(2)
driver.find_element(By.ID,"A2").click()
time.sleep(2)
all_whs=driver.window_handles
driver.switch_to.window(all_whs[1])
driver.find_element(By.NAME,"q").send_keys("selenium")
time.sleep(5)