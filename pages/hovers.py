from selene.api import *
import allure


class HoversPage:
    def __init__(self):
        self._user_pictures = ss(by.xpath("//*[@class=\"figure\"]"))
        # self._user_info = ss(by.xpath("//*[@class=\"figcaption\"]"))

    @allure.step("Open hovers page")
    def open(self):
        browser.open_url('https://the-internet.herokuapp.com/hovers')
        return self
