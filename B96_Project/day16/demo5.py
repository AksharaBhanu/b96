import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = Chrome()
driver.implicitly_wait(10)
driver.get("https://pos.aksharatraining.in/pos/public/")
print(driver.title)
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("pointofsalexxx")
driver.find_element(By.XPATH,"//button[@type='submit']").click()

try:
    driver.find_element(By.XPATH,"//a[text()='Logout']").is_displayed()
    print('PASS:Home Page is Displayed')
except:
    print('FAIL:Home Page is NOT Displayed')
