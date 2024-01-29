import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

driver = Chrome()
driver.get("file:///F:/B96%20Selenium/workspace/pages/Sample9.html?")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.ID,"A1").click()
time.sleep(2)
alert=driver.switch_to.alert
print(alert.text)
alert.dismiss()
# alert.accept()
time.sleep(2)

