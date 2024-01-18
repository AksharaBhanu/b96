import time
from selenium.webdriver import Chrome

driver=Chrome()
driver.get('https://pos.aksharatraining.in/pos/public/')
driver.set_window_size(800,900)
time.sleep(1)
x=400
y=100
for i in range(6):
    driver.set_window_position(x,y) #shift right by 100
    x=x+100
    time.sleep(1)

for i in range(6):
    driver.set_window_position(x,y) #shift down by 50
    y=y+50
    time.sleep(1)