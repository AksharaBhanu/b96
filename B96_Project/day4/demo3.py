import time
from selenium.webdriver import Chrome

driver=Chrome()
driver.get('http://www.google.com')
time.sleep(1)
element=driver.switch_to.active_element
element.send_keys('selenium')
time.sleep(4)

