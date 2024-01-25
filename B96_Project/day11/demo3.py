import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

driver = Chrome()
driver.get("https://aksharatraining.com/")
driver.maximize_window()
time.sleep(3)
join=driver.find_element(By.XPATH,"//h2[text()='Join the revolution!']")

actions=ActionChains(driver) #create object of ActionChains class
actions.scroll_from_origin(ScrollOrigin.from_element(join),0,200).perform()

time.sleep(10)