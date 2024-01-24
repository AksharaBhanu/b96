import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
driver = Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(1)
driver.find_element(By.NAME,"username").send_keys("abcd")
time.sleep(1)
driver.find_element(By.NAME,"password").send_keys("abcd")
time.sleep(1)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(2)
msg=driver.find_element(By.XPATH,"//p[text()='Invalid credentials']").text
print(msg)
#get the color for the element (css ppt) in RGB format
cRGB=driver.find_element(By.XPATH,"//p[text()='Invalid credentials']").value_of_css_property("color")
print('Color in RGB',cRGB)

#convert RGB to hexa format
cHex=Color.from_string(cRGB).hex
print('Color in Hexa',cHex)

font_size=driver.find_element(By.XPATH,"//p[text()='Invalid credentials']").value_of_css_property("font-size")
print(font_size)

font_type=driver.find_element(By.XPATH,"//p[text()='Invalid credentials']").value_of_css_property("font-family")
print(font_type)