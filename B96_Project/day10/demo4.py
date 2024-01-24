import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
driver = Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(1)
loc=driver.find_element(By.NAME,"username").location
print(loc)

x=loc['x']
print(x)

y=loc['y']
print(y)

size=driver.find_element(By.NAME,"username").size
print(size)

height=size['height']
print(height)

width=size['width']
print(width)

#Home work: verify that pw is below un
#Home work: verify that both un & pw size is same
