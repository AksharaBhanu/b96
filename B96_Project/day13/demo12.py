import time
from selenium.webdriver import Chrome
#write a code to open fb and google in 2 dif browser (selenium3)
driver1 = Chrome()
driver1.get("http://www.fb.com")
time.sleep(2)

driver2 = Chrome()
driver2.get("http://www.google.com")
time.sleep(2)




