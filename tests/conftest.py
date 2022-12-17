from selene.api import *
import allure, pytest
from selenium import webdriver

base_url = "https://the-internet.herokuapp.com"


@pytest.fixture(scope="session", autouse=True)
def setup_browser():
    # setup browser

    # capabilities = {
    #     "browserName": "firefox",
    #     "browserVersion": "108.0",
    #     "selenoid:options": {
    #         "enableVNC": True,
    #         "enableVideo": True
    #     }
    # }
    #
    # driver = webdriver.Remote(
    #     command_executor="http://localhost:4444/wd/hub",
    #     desired_capabilities=capabilities
    # )
    # browser.set_driver(driver)
    config.maximize_window = True

    # turn off selene auto-screenshots
    from selene import helpers
    helpers.take_screenshot = lambda *x: "See attachments"
    yield None


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="function")
def screenshot_on_failure(request):
    yield None
    attach = browser.driver().get_screenshot_as_png()
    if request.node.rep_setup.failed:
        allure.attach(request.function.__name__, attach, allure.attachment_type.PNG)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            allure.attach(request.function.__name__, attach, allure.attachment_type.PNG)


@pytest.fixture()
def reset_driver_state():
    browser.open_url(base_url)

    yield None
    browser.driver().delete_all_cookies()
