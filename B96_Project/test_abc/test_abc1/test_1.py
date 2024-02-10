import time


class Test_A:
    def test_1(self,open_browser):
        print(open_browser.title)
        time.sleep(1)
        for i in range(4):
            time.sleep(1)
            open_browser.switch_to.active_element.send_keys('a')
            time.sleep(1)

    def test_2(self,open_browser):
        print(open_browser.title)
        time.sleep(1)
        for i in range(4):
            time.sleep(1)
            open_browser.switch_to.active_element.send_keys('b')
            time.sleep(1)
