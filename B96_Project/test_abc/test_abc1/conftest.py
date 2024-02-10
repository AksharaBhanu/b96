# content of conftest.py
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox

import pytest

@pytest.fixture(scope="function",autouse=True,params=["firefox", "chrome"])
def open_browser(request):
    if request.param == "firefox":
        driver = Firefox()
    elif request.param == "chrome":
        driver = Chrome()
    else:
        raise ValueError("Unsupported browser: {}".format(request.param))
    driver.get('http://www.google.com')
    yield driver
    driver.quit()

