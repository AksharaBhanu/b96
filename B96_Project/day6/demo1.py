import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("file:///F:/B96%20Selenium/workspace/pages/sample2.html")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"a[id='a1']").click()
driver.back()
driver.find_element(By.CSS_SELECTOR,'a[id="a1"]').click()
time.sleep(3)