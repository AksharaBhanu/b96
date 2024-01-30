import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("file:///F:/B96%20Selenium/workspace/pages/Sample10.html")
driver.find_element(By.ID,"A5").click()
time.sleep(1)
driver.close()
all_whs=driver.window_handles
print(all_whs)
time.sleep(1)
driver.quit()
time.sleep(3)

