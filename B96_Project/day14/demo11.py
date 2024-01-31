import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.NAME,"q").send_keys("selenium")
time.sleep(1)
driver.find_element(By.NAME,"q").send_keys(Keys.ENTER)
time.sleep(2)
msg=driver.find_element(By.ID,"result-stats").text
print(msg)




