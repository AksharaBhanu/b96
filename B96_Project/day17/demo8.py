from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
url = "http://192.168.29.187:4444"
driver = webdriver.Remote(command_executor=url, options=options)
driver.get("https://aksharatraining.com/")
print(driver.title)
driver.quit()