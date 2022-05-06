import configparser  # special package

config = configparser.RawConfigParser()  # RawConfigParser is a class in configparser
config.read(r".\\Configurations\\config.ini")

"""read values from config.ini file """


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get("common info", "baseURL")
        return url

    @staticmethod
    def getEmail():
        email = config.get("common info", "email")
        return email

    @staticmethod
    def getPassword():
        password = config.get("common info", "password")
        return password
