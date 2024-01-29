import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import os

#file upload popup
driver = Chrome()
driver.get("file:///F:/B96%20Selenium/workspace/pages/Sample9.html?")
driver.maximize_window()
time.sleep(4)
# absolute_path="f:/MyCV.docx"
relative_path="./../mydoc/MyCV.docx"
absolute_path=os.path.abspath(relative_path)
print(absolute_path)
driver.find_element(By.ID,"A2").send_keys(absolute_path)
time.sleep(3)