import time

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox


@pytest.fixture(params=['firefox'])
def login(request):
    browser=request.param
    if browser=='chrome':
        driver=Chrome()
        driver.set_window_position(700,10)
    else:
        driver=Firefox()

    driver.set_window_size(700, 900)
    driver.get('http://www.google.com')

    yield driver

    driver.quit()


def test_createcustomer(login):
    driver=login
    for i in range(7):
        driver.switch_to.active_element.send_keys('a')
        time.sleep(1)

def test_editcustomer(login):
    driver=login
    for i in range(7):
        driver.switch_to.active_element.send_keys('b')
        time.sleep(1)
