import time
from selenium.webdriver import Chrome

driver=Chrome() #default size
driver.get('https://pos.aksharatraining.in/pos/public/') #enter url
# time.sleep(30) #Selenium wainting--> i will manually resize browser to req size
size=driver.get_window_size() #get new size & print
# print(size)
driver.set_window_size(800,900)
time.sleep(5)

# driver.set_window_size(size['width'],size['height'])
# time.sleep(5)