import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

#close only specific browser (ex: Swara)
expected=input("Please enter the title of the browser to be closed")
driver = Chrome()
driver.get("file:///F:/B96%20Selenium/workspace/pages/Sample10.html")
driver.find_element(By.ID,"A5").click()
time.sleep(1)
all_whs=driver.window_handles
for w in all_whs:
    driver.switch_to.window(w)
    if driver.title==expected:
        driver.close()
        break
    time.sleep(1)

time.sleep(3)
#Home work: if title is not matching it should print proper msg
