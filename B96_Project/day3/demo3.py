import time
from selenium.webdriver import Firefox
driver=Firefox() #open Firefox Browser
driver.get('http://www.google.com') #enter the url
time.sleep(3)#wait for 3s
driver.quit() #close the browser