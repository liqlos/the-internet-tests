import allure
import pytest

from pages.basic_auth import BasicAuthPage


@allure.story("http://my.jira.org/7778")
@allure.feature("Basic auth")
class TestBasicAuth:
    @allure.testcase("http://my.tms.org/TESTCASE-2")
    def test_can_authorize_with_valid_credentials(self):
        basic_auth_page = BasicAuthPage()
        basic_auth_page.open('admin', 'admin')

        assert basic_auth_page._success_text_element.text == "Congratulations! You must have the proper credentials."

    # @pytest.mark.parametrize("user, password",
    #                          [("admin", "a"), ("a", "admin"), ("", ""), ("admin", "")], )
    # def test_cant_authorize_with_invalid_credentials(self):
    #     pass
