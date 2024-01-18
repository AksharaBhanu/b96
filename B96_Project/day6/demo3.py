import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
def go_back(driver):
    time.sleep(1)
    driver.back()
    time.sleep(1)

driver=Chrome()
driver.get("file:///F:/B96%20Selenium/workspace/pages/sample2.html")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"a[id='a1']").click()
go_back(driver)
driver.find_element(By.CSS_SELECTOR,"a#a1").click()
go_back(driver)
driver.find_element(By.CSS_SELECTOR,"#a1").click()
go_back(driver)
driver.find_element(By.CSS_SELECTOR,"a[class='c1']").click()
go_back(driver)
driver.find_element(By.CSS_SELECTOR,"a.c1").click()
go_back(driver)
driver.find_element(By.CSS_SELECTOR,".c1").click()
time.sleep(3)