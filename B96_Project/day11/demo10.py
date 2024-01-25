import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

driver = Chrome()
driver.get("file:///F:/B96%20Selenium/workspace/pages/Sample8.html")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.ID,"t1").send_keys("ABC")
time.sleep(2)
driver.switch_to.frame(0) #switch to 1st frame
driver.find_element(By.ID,"t2").send_keys("XYZ")
time.sleep(2)
