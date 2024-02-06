import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

#POM class
class LoginPage:
    #declaration
    __locator=(By.NAME,"username")

    #initialization
    def __init__(self,driver):
        self.driver=driver

    #utilization
    def enter_username(self,un):
        driver.find_element(*self.__locator).send_keys(un)


driver = Chrome()
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
obj=LoginPage(driver)
obj.enter_username('admin')
