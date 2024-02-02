import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = Chrome()
driver.implicitly_wait(10)
driver.get("https://pos.aksharatraining.in/pos/public/")
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("pointofsale")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
expected ="Powered"
actual =driver.title
if expected in actual:
    print('PASS:Home Page is Displayed')
else:
    print('FAIL:Home Page is NOT Displayed')
