import time

from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome

class LoginPage:
    __username=(By.ID,"input-username")
    __password=(By.ID,"input-password")
    __gobutton=(By.NAME,"login-button")

    def __init__(self,driver):
        self.driver=driver

    def enter_username(self,un):
        self.driver.find_element(*self.__username).send_keys(un)

    def enter_password(self,pw):
        self.driver.find_element(*self.__password).send_keys(pw)

    def click_go(self):
        self.driver.find_element(*self.__gobutton).click()

driver=Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://pos.aksharatraining.in/pos/public/")

login_page=LoginPage(driver)
login_page.enter_username('admin')
login_page.enter_password('pointofsale')
login_page.click_go()

time.sleep(3)