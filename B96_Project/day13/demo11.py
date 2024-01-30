import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
driver = Chrome()
driver.get("file:///F:/B96%20Selenium/workspace/pages/Sample10.html")
parent=driver.current_window_handle
driver.find_element(By.ID,"A5").click()
time.sleep(2)
all_whs=driver.window_handles
all_whs.remove(parent)

for w in all_whs:
    driver.switch_to.window(w)
    a=driver.title
    driver.find_element(By.XPATH,"//input[@id='t1' or @id='t2']").send_keys(a)
    time.sleep(1)

time.sleep(3)
