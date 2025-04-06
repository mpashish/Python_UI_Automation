from selenium.webdriver.common.by import By

from utility.BaseClass import BaseClass
from utility.read_config_file import ReadConfig

class Login_Page(BaseClass):

    user_name_xpath = "//input[@name = 'username']"
    password_xpath = "//input[@name = 'password']"
    login_button_xpath = "//button[@type = 'submit']"

    def __init__(self, driver):
        self.driver = driver

    def enter_user_name(self):
        # self.wait_until_element_presence((By.XPATH,self.user_name_xpath))
        self.driver.find_element(By.XPATH,self.user_name_xpath).clear()
        self.driver.find_element(By.XPATH,self.user_name_xpath).send_keys(ReadConfig.get_app_user_name())

    def enter_password(self):
        self.driver.find_element(By.XPATH, self.password_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(ReadConfig.get_app_password())

    def click_on_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()
