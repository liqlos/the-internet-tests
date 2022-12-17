import allure
from pages.hovers import HoversPage


@allure.story("http://my.jira.org/7778")
@allure.feature("Basic auth")
class TestHovers:
    @allure.testcase("http://my.tms.org/TESTCASE-2")
    def test_user_info_shows_when_hover_over_profile(self):
        hovers_page = HoversPage()
        hovers_page.open()

        for picture in hovers_page._user_pictures:
            assert not picture.first_child.following_sibling().is_displayed()

            picture.hover()
            assert picture.first_child.following_sibling().is_displayed()
