from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("chrome://downloads/")
sr=driver.find_element(By.XPATH,"/html/body/downloads-manager").shadow_root
download_items=sr.find_elements(By.CSS_SELECTOR,"iron-list *")
print(len(download_items))
for items in download_items:
    print(items.tag_name)
