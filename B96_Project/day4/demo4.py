import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
driver=Chrome()
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.maximize_window()
time.sleep(3)
driver.switch_to.active_element.send_keys('admin')
time.sleep(3)
driver.switch_to.active_element.send_keys(Keys.TAB)
time.sleep(3)
driver.switch_to.active_element.send_keys('admin123')
time.sleep(3)
driver.switch_to.active_element.send_keys(Keys.ENTER)
time.sleep(6)