import time
from selenium.webdriver import Chrome
driver=Chrome()
driver.get('http://www.google.com') #goto google
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.fullscreen_window()
time.sleep(2)
driver.maximize_window()
time.sleep(3)
driver.minimize_window()
time.sleep(2)
driver.close()
