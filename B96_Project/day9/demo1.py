import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("file:///F:/B96%20Selenium/workspace/pages/sample6.html")
driver.maximize_window()
time.sleep(1)

slno=driver.find_element(By.XPATH,"//td[text()='SQL']/../td[1]").text
print('slno of SQL',slno)
cost=driver.find_element(By.XPATH,"//td[text()='SQL']/../td[3]").text
print('cost of sql',cost)
before=driver.find_element(By.XPATH,"//td[text()='SQL']/../preceding-sibling::tr[1]/td[2]").text
print('sub before sql',before)
after=driver.find_element(By.XPATH,"//td[text()='SQL']/../following-sibling::tr[1]/td[2]").text
print('sub after sql',after)
time.sleep(1)