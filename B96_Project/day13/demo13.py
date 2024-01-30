import time
from selenium.webdriver import Chrome
#write a code to open fb and google in 2 dif browser (selenium4)
driver = Chrome()
driver.get("http://www.fb.com")
time.sleep(1)

driver.switch_to.new_window('window')
driver.get("http://www.google.com")
time.sleep(2)

driver.close()

time.sleep(3)


