import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

driver = Chrome()
driver.get("http://www.dhtmlgoodies.com/submitted-scripts/i-google-like-drag-drop/")
driver.maximize_window()
time.sleep(3)

block1=driver.find_element(By.XPATH,"//h1[text()='Block 1']")
block3=driver.find_element(By.XPATH,"//h1[text()='Block 3']")
actions=ActionChains(driver)
actions.click_and_hold(block1).move_to_element(block3).pause(3).release().perform() #composite action
time.sleep(30)
