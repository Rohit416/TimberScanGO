import configparser

config = configparser.RawConfigParser()

config.read(".\\configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getURL():
        URL = config.get('common data', 'baseURL')
        return URL

    @staticmethod
    def getUsername():
        username = config.get('common data', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common data', 'password')
        return password
