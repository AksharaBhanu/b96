import time
from selenium.webdriver import Chrome

driver=Chrome() #default size
driver.get('https://pos.aksharatraining.in/pos/public/') #enter url
driver.set_window_size(800,900)
time.sleep(3)

location=driver.get_window_position()
print(location) #'x': 10, 'y': 10}
print(location['x'])
print(location['y'])

driver.set_window_position(400,200) #move the browser
time.sleep(5)