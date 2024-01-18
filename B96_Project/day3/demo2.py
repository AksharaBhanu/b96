import time
from selenium.webdriver import Edge
driver=Edge() #open Edge Browser
driver.get('http://www.google.com') #enter the url
time.sleep(3)#wait for 3s
driver.close() #close the browser