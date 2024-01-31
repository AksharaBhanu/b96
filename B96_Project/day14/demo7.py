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

#select any auto suggestion which contains 'webdriver'
msg='Not found'
option='webdriver'
for ASE in all_ASE:
    text=ASE.text
    if option in text:
        ASE.click()
        msg='Found & selected'
        break

print(option,msg)
time.sleep(4)