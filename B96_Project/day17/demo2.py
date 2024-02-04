import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC


driver = Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
wait=WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located((By.NAME,"username")))
driver.find_element(By.NAME,"username").send_keys("Admin")
time.sleep(3)