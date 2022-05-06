import pytest
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("__________________________________Test_001_Login-------------------------------------")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        act_title = self.driver.title
        self.logger.info("_____________________Verifying Home page title -------------------------------")
        if act_title == "Your store. Login":
            assert True
            self.logger.info("_________________________________Home page title passed-----------------------------")
            self.driver.close()
        else:
            self.driver.save_screenshot(r".\\Screenshots\\" + "test_homePageTitle.png")
            self.logger.error("_________________________________Home page title Failed---------------------------")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info(
            "__________________________________Verifying Log in  page-------------------------------------")

        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.set_email(self.email)
        self.lp.set_password(self.password)
        self.lp.login()
        act_logged_inPageTitle = self.driver.title
        if act_logged_inPageTitle == "Dashboard / nopCommerce administration":
            self.logger.info(
                "__________________________________Log in page test passed-------------------------------------")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(r".\\Screenshots\\" + "test_login.png")
            self.logger.error(
                "__________________________________Log in page test Failed-------------------------------------")
            self.driver.close()
            assert False
