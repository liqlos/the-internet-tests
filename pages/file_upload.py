from selene.api import *
import allure, pytest


class FileUpload:
    def __init__(self):
        self._file_upload_element = s(by.id("file-upload"))
        self._file_submit_button = s(by.id("file-submit"))
        self._success_text = s(by.xpath("//h3"))
        self._uploaded_file_name = s(by.id("uploaded-files"))

    @allure.step("Open file upload page")
    def open(self):
        browser.open_url('https://the-internet.herokuapp.com/upload')
        return self

    @allure.step("Upload file [{1}]")
    def upload_file(self, file_path):
        self._file_upload_element.send_keys(file_path)
        self._file_submit_button.submit()

