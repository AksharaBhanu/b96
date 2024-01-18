from selenium.webdriver import Chrome
driver=Chrome()

driver.get('http://www.fb.com')

t=driver.title
print(t)

url=driver.current_url
print(url)

html_code=driver.page_source
print(html_code)
