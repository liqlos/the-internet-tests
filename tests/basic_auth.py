from common_imports import *
from pages.basic_auth import BasicAuthPage


@allure.story("http://my.jira.org/7778")
@allure.feature("Basic auth")
class BasicAuthTests:
    @allure.testcase("http://my.tms.org/TESTCASE-2")
    def test_can_authorize_with_valid_credentials(self):
        basic_auth_page = BasicAuthPage.open("admin", "admin")
        assert basic_auth_page._success_text_element.text == "Congratulations! You must have the proper credentials."