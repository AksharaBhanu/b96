import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.NAME,"username").send_keys("admin")
time.sleep(1)
driver.find_element(By.NAME,"password").send_keys("admin123")
time.sleep(1)
driver.find_element(By.TAG_NAME,"button").click()
time.sleep(4)

