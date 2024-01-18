import time
from selenium.webdriver import Chrome
driver=Chrome()
driver.get('file:///F:/B96%20Selenium/pages/sample1.html')
print(driver.title)
time.sleep(3)
driver.quit()