from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# driver=Chrome()
# driver.get("http://www.google.com")
# print(driver.title)
# driver.quit()
#

options = Options()
url = "https://username:accesskey@ondemand.eu-central-1.saucelabs.com:443/wd/hub"
driver = webdriver.Remote(command_executor=url, options=options)
driver.get("https://aksharatraining.com/")
print(driver.title)
driver.quit()