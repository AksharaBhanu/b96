import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

driver = Chrome()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
time.sleep(3)
button=driver.find_element(By.XPATH,"//span[text()='right click me']")
actions=ActionChains(driver)
actions.context_click(button).perform()
time.sleep(1)
driver.find_element(By.XPATH,"//span[text()='Copy']").click()
time.sleep(3)
