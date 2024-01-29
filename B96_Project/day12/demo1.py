import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

#Frame popup
driver = Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
time.sleep(3)
driver.switch_to.frame(0)
driver.find_element(By.XPATH,"//button[text()='Stay signed out']").click()
driver.switch_to.default_content()
time.sleep(2)
driver.find_element(By.NAME,"q").send_keys("selenium")
time.sleep(4)
