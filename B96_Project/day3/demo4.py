import time
from selenium.webdriver import Chrome
driver=Chrome()
driver.get('http://www.google.com') #goto google
time.sleep(2)
driver.get('http://www.fb.com') #goto fb
time.sleep(2)
driver.back() #go back to google
time.sleep(2)
driver.forward() #go to fb
time.sleep(2)
driver.refresh() #refresh/reload the page
time.sleep(2)

