import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

driver = Chrome()
driver.get("https://www.plus2net.com/javascript_tutorial/ondblclick-demo.php")
driver.maximize_window()
time.sleep(3)
before=driver.find_element(By.ID,"box").text
print(before)

button=driver.find_element(By.XPATH,"//input[@value='Double Click']")
actions=ActionChains(driver)
actions.double_click(button).perform()
time.sleep(1)

after=driver.find_element(By.ID,"box").text
print(after)

time.sleep(3)

#home work: print the background color