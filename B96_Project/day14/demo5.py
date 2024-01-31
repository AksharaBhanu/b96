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

#count the number of auto suggestions
count=len(all_ASE)
print('Number of auto suggestions',count)

#print all the auto suggestions
for ASE in all_ASE:
    print(ASE.text)

#select 1st  auto suggestion
# all_ASE[0].click()

#select last  auto suggestion
# all_ASE[count-1].click()

#select 4th  auto suggestion
all_ASE[3].click()


time.sleep(4)


