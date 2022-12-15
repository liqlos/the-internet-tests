from common_imports import *


class BasicAuthPage:
    def __init__(self):
        self._success_text_element = s(by.xpath("//*/p"))

    @allure.step("Opening basic auth page and authorizing")
    def open(self, user, password):
        browser.open_url('https://' + user + ":" + password + '@the-internet.herokuapp.com/basic_auth')
        return self
