import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

#how to handle dropdown menu: mouse hover
driver = Chrome()
driver.get("https://www.globalsqa.com/")
driver.maximize_window()
time.sleep(2)
menu=driver.find_element(By.XPATH,"(//a[text()='Free Ebooks'])[1]")
actions=ActionChains(driver)
actions.move_to_element(menu).perform()
time.sleep(1)
driver.find_element(By.XPATH,"(//span[text()='Free Machine Learning Ebooks'])[1]").click()
time.sleep(4)
#Home work : Select Tester’s Hub->Demo Testing Site->Tooltip
