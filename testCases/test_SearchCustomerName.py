import time
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.AddCustomers import AddCustomer
from pageObjects.SearchCustomers import SearchCustomerData


class Test_005_SearchCustomer_Login:
    baseURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_addCustomerDetails(self, setup):
        self.logger.info("******************Test_005_SearchCustomer*************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(3)
        lp = Login(self.driver)
        lp.set_email(self.email)
        lp.set_password(self.password)
        lp.login()
        self.logger.info("****************************Login was successful***********************")

        self.logger.info("*******************************Search Customer Test ******************************")
        add_customer = AddCustomer(self.driver)  # Class is being initialised
        add_customer.click_customersMenu()  # entering to customers page
        add_customer.click_customerMenuItem()

        self.logger.info("***************Enter details of existing customer to search through Name********************")
        search_data = SearchCustomerData(self.driver)
        search_data.search_firstname("James")
        search_data.search_lastname("Pan")
        search_data.search_btn()
        time.sleep(3)
        status = search_data.customerSearchName("James Pan")
        print(status)
        assert status == True

        self.driver.close()
        self.logger.info("*********************Test_005_SearchCustomer successful***********************")
