import pytest
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData//LoginData.xlsx"
    logger = LogGen.loggen()
    lst_value = []

    def test_login(self, setup):
        self.logger.info("********************************Test_002_DDT_Login*********************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info(
            "__________________________________Verifying Log in  page-------------------------------------")

        self.driver.maximize_window()
        self.lp = Login(self.driver)

        self.rows = XLUtils.getRowCount(self.path, "sheet1")
        print(f"Number of rows in excel sheet:{self.rows}")

        for r in range(2, self.rows+1):
            self.user = XLUtils.readData(self.path, "sheet1", r, 1)
            self.passwd = XLUtils.readData(self.path, "sheet1", r, 2)
            self.expected = XLUtils.readData(self.path, "sheet1", r, 3)
            self.lp.set_email(self.user)
            self.lp.set_password(self.passwd)
            self.lp.login()

        act_title = self.driver.title
        exp_title = "Dashboard / nopCommerce administration"

        if act_title == exp_title:
            if self.expected == "pass":
                self.logger.info("**************Test Passed****************")
                self.lp.logout()
                self.lst_value.append("pass")
            elif self.expected == "Fail":
                self.logger.info("***************Test FAILED***************")
                self.lp.logout()
                self.lst_value.append("Fail")
        elif act_title != exp_title:
            if self.expected == "pass":
                self.logger.info("***************Test FAILED***************")
                self.lp.logout()
                self.lst_value.append("Fail")
            elif self.expected == "Fail":
                self.logger.info("***************Test Passed***************")
                self.lp.logout()
                self.lst_value.append("Pass")

        if "Fail" not in self.lst_value:
            self.logger.info("***************Test_002_DDT_Login test cases Passed***************")
            self.driver.close()
            assert True
        else:
            self.logger.info("***************Test_002_DDT_Login test cases Failed***************")
            self.driver.close()
            assert False

        self.logger.info("End of Login DDT Test")
        self.logger.info("Completed Test_002_DDT_Test_Login")








