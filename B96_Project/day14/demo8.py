import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("https://www.amazon.in//")
driver.maximize_window()
time.sleep(2)
all_links=driver.find_elements(By.XPATH,"//a")
count=len(all_links)
print(count)
i=1
for link in all_links:
    print(i,'Displayed',link.is_displayed())
    i=i+1

#count the number of hidden links
i=1
for link in all_links:
   if not(link.is_displayed()):
    i=i+1

print('Hidden links',i)