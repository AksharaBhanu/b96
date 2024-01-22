import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("file:///F:/B96%20Selenium/workspace/pages/sample6.html")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH,"//td[text()='API']/../td[4]/input").click()

time.sleep(5)
