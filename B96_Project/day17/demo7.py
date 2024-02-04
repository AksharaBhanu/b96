from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

options = FirefoxOptions()
options.browser_version = 'latest'
options.platform_name = 'Linux'
sauce_options = {}
sauce_options['username'] = '--------'
sauce_options['accessKey'] = '------'
sauce_options['build'] = '2.34'
sauce_options['name'] = 'Test1_Akshara'
options.set_capability('sauce:options', sauce_options)
url = "https://ondemand.eu-central-1.saucelabs.com:443/wd/hub"
driver = webdriver.Remote(command_executor=url, options=options)
driver.get("https://aksharatraining.com/")
print(driver.title)
driver.quit()