from common_imports import *
from pages.hovers import HoversPage


@allure.story("http://my.jira.org/7778")
@allure.feature("Basic auth")
class HoversTests:
    @allure.testcase("http://my.tms.org/TESTCASE-2")
    def test_user_info_shows_when_hover_on_profile(self):
        hovers_page = HoversPage.open("admin", "admin")

        for index, picture in enumerate(hovers_page._user_pictures, 1):
            picture.hover()
            hovers_page._user_info(index).should(be.visible)

