import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ChromeService

s=ChromeService('../driver/chromedriver.exe')
driver=Chrome(service=s)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://www.trizettoprovider.com/')
menu=driver.find_element(By.XPATH,"//a[text()='Who We Are']")
actions=ActionChains(driver)
actions.move_to_element(menu).perform()
time.sleep(2)
os=driver.find_element(By.XPATH,"//a[text()='Our Story']")
actions=ActionChains(driver)
actions.move_to_element(os).perform()
time.sleep(1)
os.click()
time.sleep(4)