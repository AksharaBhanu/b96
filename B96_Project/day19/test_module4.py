from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

def test_orange_login():

    driver = Chrome()
    driver.implicitly_wait(10)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    driver.find_element(By.NAME,"username").send_keys('admin')
    driver.find_element(By.NAME,"password").send_keys('admin123')
    driver.find_element(By.XPATH,"//button[@type='submit']").click()

    actual=driver.current_url
    expected='cashboard'
    assert expected in actual



