import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.NAME,"q").send_keys("selenium")
time.sleep(2)
xp="//span[contains(text(),'selenium')]"

all_ASE=driver.find_elements(By.XPATH,xp)

#select selenium tutorial
msg='Not found'
option='selenium bhanu'
for ASE in all_ASE:
    text=ASE.text
    if text==option:
        ASE.click()
        msg='Found & selected'
        break

print(option,msg)
time.sleep(4)


