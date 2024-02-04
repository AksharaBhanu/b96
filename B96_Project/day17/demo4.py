
from selenium.webdriver import Chrome
from datetime import datetime

driver = Chrome()
print(driver.timeouts.page_load) #300s--> 5M
print(driver.timeouts.script)
driver.set_script_timeout(10)
driver.set_page_load_timeout(10)

try:
    start=datetime.now()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    end = datetime.now()
    diff=end-start
    print('Page is loaded within:',diff)
except:
    print('Page is NOT loaded within 5s')
