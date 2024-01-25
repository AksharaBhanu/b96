import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

driver = Chrome()
driver.get("file:///F:/B96%20Selenium/workspace/pages/Sample8.html")
driver.maximize_window()
time.sleep(2)

driver.switch_to.frame(0) #switch to 1st frame-using index
driver.find_element(By.ID,"t2").send_keys("X")
time.sleep(1)
driver.switch_to.default_content() #exit from frame and goto main page
driver.find_element(By.ID,"t1").send_keys("A")
time.sleep(1)

driver.switch_to.frame("f1")#switch to frame-using id of the frame
driver.find_element(By.ID,"t2").send_keys("Y")
time.sleep(1)
driver.switch_to.default_content() #exit from frame and goto main page
driver.find_element(By.ID,"t1").send_keys("B")
time.sleep(1)

frameElement=driver.find_element(By.XPATH,"//iframe[@name='n1']")
driver.switch_to.frame(frameElement) #switch into frame using frame element
driver.find_element(By.ID,"t2").send_keys("Z")
time.sleep(1)
driver.switch_to.default_content() #exit from frame and goto main page
driver.find_element(By.ID,"t1").send_keys("C")
time.sleep(3)
