import time
from selenium.webdriver import Chrome

driver=Chrome()
driver.get('http://www.fb.com')
time.sleep(2)

size=driver.get_window_size() #get current size of the browser
print(size)

w=size['width']
print(w)

h=size['height']
print(h)


driver.set_window_size(600,600) #resize the browser
time.sleep(3)