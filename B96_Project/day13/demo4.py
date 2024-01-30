import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

#print title of all the child browsers
driver = Chrome()
driver.get("file:///F:/B96%20Selenium/workspace/pages/Sample10.html")
parent=driver.current_window_handle
time.sleep(2)
driver.find_element(By.ID,"A5").click()
time.sleep(2)
all_whs=driver.window_handles

# for i in range(1,len(all_whs)):
#     driver.switch_to.window(all_whs[i])
#     print(driver.title)

all_whs.remove(parent)
for w in all_whs:
    driver.switch_to.window(w)
    print(driver.title)

time.sleep(2)