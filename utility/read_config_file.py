import configparser

parser = configparser.RawConfigParser()
parser.read("D:\\OneDrive - Fulcrum Digital\\Desktop\\Python\\Frameworks\\Python_UI_Automation\\configuration\\config.ini")

class ReadConfig:

    @staticmethod
    def get_app_url():
        url = parser.get("login details","url")
        return url

    @staticmethod
    def get_app_user_name():
        username = parser.get("login details", "username")
        return username

    @staticmethod
    def get_app_password():
        password = parser.get("login details", "password")
        return password