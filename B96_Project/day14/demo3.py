import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrom_option=Options()
chrom_option.add_argument("--disable-notifications")
driver = Chrome(options=chrom_option) #open chrome browser specified settings
driver.get("https://www.irctc.co.in/nget/train-search")
time.sleep(10)
