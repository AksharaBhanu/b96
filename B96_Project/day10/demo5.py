import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
driver = Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(1)
logo=driver.find_element(By.XPATH,"//img[@alt='company-branding']")
logo.screenshot('mylogo.png') #take screenshot of specified element

driver.get_screenshot_as_file('loginpage.png')#take screenshot of complete page
