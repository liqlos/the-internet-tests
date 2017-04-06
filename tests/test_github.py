from common_imports import *
from pages.github.explore_tab import ProjectShowcasesGrid
from pages.github.general import Header, SignUpForm, SearchResultsPage
from pages.github.pages_resource import PagesIndex
from helpers import random_string


@allure.story("Explore Tab")
@allure.feature("Sample suite")
@pytest.mark.usefixtures("reset_driver_state", "screenshot_on_failure")
class TestExplore:
    @allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.testcase("http://my.tms.org/TESTCASE-1")
    @pytest.mark.parametrize("showcase_title", ["Open data", "Tools for Open Source", "Design essentials"])
    def test_number_of_project_showcase_supported_languages_is_the_same_on_preview_and_showcase_page_and_tooltip(self,
                                                                                                                 showcase_title):
        Header().open_menu_item("Explore")
        showcase_preview = ProjectShowcasesGrid().find_showcase(showcase_title)
        preview_languages_number = showcase_preview.get_supported_languages_number()
        showcase_details = showcase_preview.open_details()

        details_languages_number = showcase_details.get_supported_languages_number()
        tooltip_languages_number = showcase_details.get_number_of_languages_in_tooltip()

        self.verify_preview_and_details_and_tooltip_has_the_same_language_number(preview_languages_number,
                                                                                 details_languages_number,
                                                                                 tooltip_languages_number)

    @allure.step("verify preview({1}) and details({2}) and tooltip({3}) has the same language number")
    def verify_preview_and_details_and_tooltip_has_the_same_language_number(self, preview_languages_number,
                                                                            details_languages_number,
                                                                            tooltip_languages_number):
        assert preview_languages_number == details_languages_number == tooltip_languages_number, \
            "Showcase supported languages number in preview, details and tooltip expected to be equal"


@allure.story("Registration Form")
@allure.feature("Sample suite")
@pytest.mark.usefixtures("reset_driver_state", "screenshot_on_failure")
class TestRegistrationForm:
    @allure.severity(pytest.allure.severity_level.MINOR)
    @allure.testcase("http://my.tms.org/TESTCASE-2")
    @pytest.mark.parametrize("top_info_message,username_info_message,email_info_message,password_info_message",
                             [("There were problems creating your account.", "Login can't be blank",
                               "Email can't be blank",
                               "Password can't be blank and is too short (minimum is 7 characters)")])
    def test_empty_values_in_sign_up_form_show_info_messages(self, top_info_message, username_info_message,
                                                             email_info_message, password_info_message):
        sign_up_form = SignUpForm()

        sign_up_form \
            .set_username("") \
            .set_email("") \
            .set_password("") \
            .click_sign_up()

        sign_up_form \
            .top_info_message_should(be.visible) \
            .top_info_message_should(have.exact_text(top_info_message)) \
            .username_info_message_should(be.visible) \
            .username_info_message_should(have.exact_text(username_info_message)) \
            .email_info_message_should(be.visible) \
            .email_info_message_should(have.exact_text(email_info_message)) \
            .password_info_message_should(be.visible) \
            .password_info_message_should(have.exact_text(password_info_message))

    @allure.severity(pytest.allure.severity_level.TRIVIAL)
    @allure.testcase("http://my.tms.org/TESTCASE-3")
    def test_username_and_email_field_data_is_not_lost_in_case_of_incorrect_registration_attempt(self):
        sign_up_form = SignUpForm()
        username = random_string()
        email = random_string()

        sign_up_form \
            .set_username(username) \
            .set_email(email) \
            .set_password("") \
            .click_sign_up()

        sign_up_form \
            .username_input_should(have.value(username)) \
            .email_input_should(have.value(email))


@allure.story("Search")
@allure.feature("Sample suite")
@pytest.mark.usefixtures("reset_driver_state", "screenshot_on_failure")
class TestSearch:
    @allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.testcase("http://my.tms.org/TESTCASE-5")
    def test_search_redirects_to_search_page(self):
        header = Header()
        search_results_page = SearchResultsPage()
        query = random_string()

        header.search_for(query)

        search_results_page \
            .tab_should("Repositories", be.visible) \
            .tab_should("Code", be.visible) \
            .tab_should("Commits", be.visible) \
            .tab_should("Issues", be.visible) \
            .tab_should("Wikis", be.visible) \
            .tab_should("Users", be.visible)

        header.search_input_should(have.value(query))


@allure.story("Pages")
@allure.feature("Sample suite")
@pytest.mark.usefixtures("screenshot_on_failure")
class TestPageSearch:
    @pytest.fixture()
    def reset_driver_state(self):
        browser.visit("https://pages.github.com/")

        yield None
        browser.driver().delete_all_cookies()

    @allure.severity(pytest.allure.severity_level.NORMAL)
    @allure.testcase("http://my.tms.org/TESTCASE-4")
    @pytest.mark.parametrize("git_client_tab,visible_steps",
                             [("A terminal", ["Clone the repository", "Hello World", "Push it"]),
                              ("GitHub for Windows", ["Clone the repository", "Create an index file", "Commit & sync"]),
                              ("GitHub for Mac", ["Clone the repository", "Create an index file", "Commit & sync"]),
                              ("I don't know", ["Download GitHub for Windows", "Clone the repository", "Create an index file", "Commit & sync"])
                              ])
    def test_pages_github_flows_for_user_site_tab(self, reset_driver_state, git_client_tab, visible_steps):
        common_steps = ["Create a repository", "What git client are you using?", "…and you're done!"]
        common_steps[2:2] = visible_steps
        # visible_steps.update(common_steps)
        pages_index = PagesIndex()

        pages_index.select_user_or_organization_site()
        pages_index.select_client_tab(git_client_tab)

        pages_index.verify_steps(common_steps)

    @allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.testcase("http://my.tms.org/TESTCASE-6")
    @allure.issue("http://jira.lan/browse/ISSUE-1")
    def test_that_always_fails(self):
        with allure.step("Example failing step"):
            assert 2 == 3, "Intentional fail"
