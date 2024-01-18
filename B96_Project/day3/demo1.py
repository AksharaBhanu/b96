import time
from selenium.webdriver import Chrome
driver=Chrome()  #open the chrome browser
driver.get('http://www.google.com') #enter the url & open the page
time.sleep(3) #wait for 3Sec
driver.close() #close the browser