import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("file:///F:/B96%20Selenium/workspace/pages/Sample7.html")
time.sleep(2)
driver.find_element(By.ID,"A2").click()
time.sleep(2)
all_whs=driver.window_handles
print('Tab count',len(all_whs))
for wh in all_whs:
    driver.switch_to.window(wh)
    print(driver.title)
    driver.close()
    time.sleep(1)

# driver.close()
# driver.quit()
time.sleep(3)