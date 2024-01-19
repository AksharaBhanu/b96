import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
