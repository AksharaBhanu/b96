import time
from selenium.webdriver import Chrome

driver=Chrome()
driver.get('https://pos.aksharatraining.in/pos/public/')
driver.set_window_size(800,700)
time.sleep(1)
x=100
y=100
for i in range(10):
    driver.set_window_position(x,y)
    x+=50
    y+=50
    time.sleep(1)
