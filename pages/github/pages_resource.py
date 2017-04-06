from common_imports import *


class PagesIndex:
    def __init__(self):
        self._user_site_tab = s("a[href$=user-site]")
        self._project_site_tab = s("a[href$=project-site]")
        self._visible_steps = ss("ul#user-site > li:not(.hidden)")

    @allure.step
    def select_user_or_organization_site(self):
        self._user_site_tab.scroll_to().click()
        return self

    @allure.step
    def select_project_site(self):
        self._project_site_tab.click()
        return self

    @allure.step("select client tab '{1}'")
    def select_client_tab(self, text):
        self.get_client_tab(text).scroll_to().click()
        return self

    @allure.step("verify steps {1}")
    def verify_steps(self, *args):
        for i in range(len(args[0])):
            self._visible_steps[i].scroll_to().should(be.visible)
            self._visible_steps[i].element("h4").should(have.exact_text(args[0][i]))

    def get_step_area(self, title):
        return s(by.xpath("//ul[@id='user-site']/li[not(contains(@class, 'hidden')) and h4[.='%s']]" % title))

    def get_client_tab(self, text):
        return s("#user-site .question").s(by.link_text(text))
