import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

driver = Chrome()
driver.get("https://aksharatraining.com/")
driver.maximize_window()
time.sleep(2)

# driver.execute_script("window.scrollBy(0,3000)")
e=driver.find_element(By.XPATH,"//span[text()='WHY AKSHARA TRAINING']")

actions=ActionChains(driver)
actions.scroll_to_element(e).perform()
time.sleep(2)

actions.scroll_from_origin(ScrollOrigin.from_element(e),0,500).perform()
time.sleep(30)