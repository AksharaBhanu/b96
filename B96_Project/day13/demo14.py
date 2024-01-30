import time
from selenium.webdriver import Chrome
#write a code to open fb in 1st tab and google in 2nd tab (only in selenium4)
driver = Chrome()
driver.get("http://www.fb.com")
time.sleep(1)

driver.switch_to.new_window('tab')
driver.get("http://www.google.com")
time.sleep(3)