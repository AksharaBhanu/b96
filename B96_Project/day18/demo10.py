import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.find_element(By.NAME,"username").send_keys('a')

LT=By.NAME
LV="username"
driver.find_element(LT,LV).send_keys('d')

locator=(LT,LV)
driver.find_element(locator[0],locator[1]).send_keys('m')

driver.find_element(*locator).send_keys('i')

time.sleep(3)

