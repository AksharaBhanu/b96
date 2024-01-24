import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
driver = Chrome()
driver.get("https://www.google.com/")
driver.execute_script("alert('Hi')")
time.sleep(3)