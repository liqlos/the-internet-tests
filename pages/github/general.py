from common_imports import *
from selene.conditions import text


class Header:
    def __init__(self):
        self._menu_items = ss("a.nav-item")
        self._search_input = s(".header-search [name=q]")
        self._sign_in_link = s(".site-header-link").s(by.link_text("Sign in"))
        self._sign_in_link = s(".site-header-link").s(by.link_text("Sign out"))

    @allure.step("open menu item [{1}]")
    def open_menu_item(self, item):
        self._menu_items.element_by(text(item)).click()
        return self

    @allure.step("search for {1}")
    def search_for(self, query):
        self._search_input.set(query).submit()
        return self

    @allure.step("search input should {1}")
    def search_input_should(self, condition):
        self._search_input.should(condition)
        return self


class Footer:
    pass


class SignUpForm:
    def __init__(self):
        # controls:
        self._username_input = s("input[name='user[login]']")
        self._email_input = s("input[name='user[email]']")
        self._password_input = s("input[name='user[password]']")
        self._sign_up_button = s(".js-signup-form button")

        # info messages:
        self._top_info_message = s(".js-signup-form h2 + div.flash-error")
        self._username_info_message = s(
            by.xpath("//input[@name='user[login]']//ancestor::dl[contains(@class,'form-group')]/dd[@class='error']"))
        self._email_info_message = s(
            by.xpath("//input[@name='user[email]']//ancestor::dl[contains(@class,'form-group')]/dd[@class='error']"))
        self._password_info_message = s(
            by.xpath("//input[@name='user[password]']//ancestor::dl[contains(@class,'form-group')]/dd[@class='error']"))

    @allure.step("set username[{1}]")
    def set_username(self, username):
        self._username_input.set(username)
        return self

    @allure.step("set email[{1}]")
    def set_email(self, email):
        self._email_input.set(email)
        return self

    @allure.step("set password[{1}]")
    def set_password(self, password):
        self._password_input.set(password)
        return self

    @allure.step("click sign up button")
    def click_sign_up(self):
        self._sign_up_button.click()
        return self

    @allure.step("username input should {1}")
    def username_input_should(self, condition):
        self._username_input.should(condition)
        return self

    @allure.step("email input should {1}")
    def email_input_should(self, condition):
        self._email_input.should(condition)
        return self

    @allure.step("password input should {1}")
    def password_input_should(self, condition):
        self._password_input.should(condition)
        return self

    @allure.step("top info message should {1}")
    def top_info_message_should(self, condition):
        self._top_info_message.should(condition)
        return self

    @allure.step("username info message should {1}")
    def username_info_message_should(self, condition):
        self._username_info_message.should(condition)
        return self

    @allure.step("email info message should {1}")
    def email_info_message_should(self, condition):
        self._email_info_message.should(condition)
        return self

    @allure.step("password info message should {1}")
    def password_info_message_should(self, condition):
        self._password_info_message.should(condition)
        return self


class SearchResultsPage:
    def __init__(self):
        self._tabs_area = s(".underline-nav")
        self._advanced_search_link = s(".underline-nav + div a")

    @allure.step("'{1}' search result tab should {2}")
    def tab_should(self, tab_title, condition):
        self._tabs_area.element(by.link_text(tab_title)).should(condition)
        return self
