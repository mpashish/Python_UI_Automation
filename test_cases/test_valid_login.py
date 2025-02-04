import inspect

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v130.dom import discard_search_results

from base_pages.LoginPage import Login_Page
from utility.BaseClass import BaseClass

# @pytest.mark.usefixtures("setup")
class Test_Application_Login(BaseClass):

    def test_valid_login_title(self,setup):
        log = BaseClass.get_log_object(self)
        self.wait_for_page_load(10)
        login_page = Login_Page(self.driver)
        log.info("Initiated browser **************************** ")
        login_page.enter_user_name()
        login_page.enter_password()
        log.info("Entered user name and password *******************")
        login_page.click_on_login_button()
        self.verify_page_title("OrangeHRM *******************")
        log.info("Title verified ")

    def test_InValid_login_title(self,setup):
        log = BaseClass.get_log_object(self)
        self.wait_for_page_load(10)
        login_page = Login_Page(self.driver)
        login_page.enter_user_name()
        login_page.enter_password()
        log.info("Entered user name and password")
        login_page.click_on_login_button()
        self.verify_page_title("angeHRM")
        log.info("Verified invalid login ")