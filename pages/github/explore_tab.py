from common_imports import *
from selene.elements import SeleneElement
from selene.conditions import text

def get_number(details_text):
    return int(details_text.split(" ")[0])

class ShowcasePreview:
    def __init__(self, container: SeleneElement, title):
        self._container = container
        self._title = title
        details = self._container.elements(".exploregrid-item-meta-details")
        self._repo_details = details[0]
        self._language_details = details[1]

    @allure.step
    def open_details(self):
        self._container.element("a").click()
        return ShowcaseDetails()

    @allure.step("verify supported languages number[{1}]")
    def verify_supported_languages_number(self, number):
        assert number == self.get_supported_languages_number(), "Showcase preview element '%s' expected to have %s " \
                                                                "number of supported languages" % (self._title, number)

    @allure.step
    def get_supported_languages_number(self):
        return get_number(self._language_details.text)


class ShowcaseDetails:
    def __init__(self):
        self._title = s(".showcase-page-header h1")
        self._description = s(".showcase-page-description")
        details = ss(".showcase-page-header .meta-info")
        self._repo_details = details[0]
        self._language_details = details[1]
        self._update_details = details[2]

    @allure.step
    def get_supported_languages_number(self):
        return get_number(self._language_details.text)

    @allure.step
    def get_number_of_languages_in_tooltip(self):
        return len(self._language_details.get_attribute("aria-label").split(","))


class ProjectShowcasesGrid:
    def __init__(self):
        self._showcases_list = ss(".exploregrid li")
        self._more_showcases_button = s(by.partial_link_text("More showcases"))
        self._previous_page = ss(".pagination").element_by(text("Previous"))
        self._next_page = ss(".pagination").element_by(text("Next"))
        self._search_showcases_input = s(".collection-listing-search [name=q]")

    @allure.step("find showcase[{1}]")
    def find_showcase(self, title: str) -> ShowcasePreview:
        return ShowcasePreview(self._showcases_list.element_by(text(title)), title)
