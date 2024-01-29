import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

#file upload popup
driver = Chrome()
driver.get("file:///F:/B96%20Selenium/workspace/pages/Sample9.html?")
driver.maximize_window()
time.sleep(4)
driver.find_element(By.ID,"A2").send_keys("f:/MyCV.docx") # we have used obsolute path
time.sleep(3)