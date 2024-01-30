import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

#print title of all the browsers
driver = Chrome()
driver.get("file:///F:/B96%20Selenium/workspace/pages/Sample10.html")
time.sleep(2)
driver.find_element(By.ID,"A5").click() # it will display 2 child windows
time.sleep(2)
all_whs=driver.window_handles

for w in all_whs:
    driver.switch_to.window(w)
    print(driver.title)

time.sleep(2)