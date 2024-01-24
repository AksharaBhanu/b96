import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
driver = Chrome()
driver.get("https://aksharatraining.com/")
driver.get_screenshot_as_file('akshara.png')#take screenshot of  current visible area of the page
print('done')
driver.quit()
