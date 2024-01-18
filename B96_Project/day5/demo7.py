import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

time.sleep(2)
un=driver.find_element(By.NAME,"username")
un.send_keys("admin")
un.send_keys(Keys.CONTROL+"a")
un.send_keys(Keys.CONTROL+"c")

time.sleep(1)
pw=driver.find_element(By.NAME,"password")
pw.send_keys(Keys.CONTROL+"v")
pw.send_keys("123")
time.sleep(1)

driver.find_element(By.TAG_NAME,"button").click()
time.sleep(4)

