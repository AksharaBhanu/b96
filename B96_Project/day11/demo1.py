import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains

driver = Chrome()
driver.get("https://aksharatraining.com/")
driver.maximize_window()
time.sleep(3)

actions=ActionChains(driver) #create object of ActionChains class

for i in range(7):
    actions.scroll_by_amount(0,500).perform()   #scroll down
    time.sleep(1)

for i in range(7):
    actions.scroll_by_amount(0,-500).perform() #scroll up
    time.sleep(1)

time.sleep(3)