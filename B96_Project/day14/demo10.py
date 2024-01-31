import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

#print content of the table
driver = Chrome()
driver.get("file:///F:/B96%20Selenium/workspace/pages/sample5.html")
driver.maximize_window()
time.sleep(2)
all_cells=driver.find_elements(By.XPATH,"//td|//th")
for cell in all_cells:
    print(cell.text)

#home work:print the content of table in table format
