import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("file:///F:/B96%20Selenium/workspace/pages/Sample10.html")
cwh=driver.current_window_handle
print(cwh)
time.sleep(2)
driver.find_element(By.ID,"A5").click() # it will display 2 child windows
time.sleep(2)
allwhs=driver.window_handles
print(len(allwhs)) #number of whs
for w in allwhs:
    print(w)


