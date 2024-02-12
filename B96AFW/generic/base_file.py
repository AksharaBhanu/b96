import pytest
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver.support.wait import WebDriverWait
from pyjavaproperties import Properties

class BaseTest:

    @pytest.fixture(autouse=True)
    def pre_condition(self):
        p = Properties()
        p.load(open('../config.properties'))
        browser=p['BROWSER']
        app_url=p['APP_URL']
        ito=p['ITO']
        eto=p['ETO']

        if browser.lower()=='firefox':
            self.driver=Firefox()
        else:
            self.driver=Chrome()

        self.driver.get(app_url)
        self.driver.implicitly_wait(ito)
        self.wait=WebDriverWait(self.driver,eto)
        self.driver.maximize_window()

    @pytest.fixture(autouse=True)
    def post_condtion(self):
        yield
        self.driver.close()