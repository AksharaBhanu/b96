import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

for i in range(100):
    try:
        driver.find_element(By.NAME,"username").send_keys("Admin")
        print('element found & action performed',i)
        break
    except:
        print('element Not found & we will re-try')

time.sleep(3)