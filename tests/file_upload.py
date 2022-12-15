import os
from common_imports import *
from pages.file_upload import FileUpload


@allure.story("http://my.jira.org/7777")
@allure.feature("File upload")
class FileUploadTests:
    @allure.testcase("http://my.tms.org/TESTCASE-1")
    def test_can_upload_file(self):
        file_name = "1.jpeg"
        file_path = os.path.dirname(os.path.abspath(__file__)) + "/resources/" + file_name
        file_upload_page = FileUpload()

        file_upload_page.open().upload_file(file_path)
        assert file_upload_page._success_text.text == "File Uploaded!"
        assert file_upload_page._uploaded_file_name.text == file_name

