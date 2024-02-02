import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = Chrome()
print(driver.timeouts.implicit_wait)
driver.implicitly_wait(10)
print(driver.timeouts.implicit_wait)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element(By.NAME,"username").send_keys("Admin")
time.sleep(3)