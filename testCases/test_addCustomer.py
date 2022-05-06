import time
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.AddCustomers import AddCustomer
import random
import string


def random_email_generator(size=8, chars=(string.ascii_lowercase + string.digits)):
    return "".join(random.choice(chars) for i in range(size))


class Test_003_AddCustomer_Login:
    baseURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_addCustomerDetails(self, setup):
        self.logger.info("******************Test_003_AddCustomer_Login*************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(3)
        lp = Login(self.driver)
        lp.set_email(self.email)
        lp.set_password(self.password)
        lp.login()
        self.logger.info("****************************Login was successful***********************")

        self.logger.info("*******************************Add Customer Test ******************************")
        add_customer = AddCustomer(self.driver)  # Class is being initialised
        add_customer.click_customersMenu()  # entering to customers page
        add_customer.click_customerMenuItem()
        add_customer.click_AddNewButton()  # to add new customer

        self.logger.info("*************************Adding Customer info details***************************************")
        self.generated_email = random_email_generator() + "@gmail.com"
        add_customer.input_email(self.generated_email)
        time.sleep(3)
        add_customer.input_password("Hello123@")
        add_customer.input_FirstName("Srikanth")
        time.sleep(3)
        add_customer.input_LastName("Yadav")
        add_customer.set_gender("Male")
        add_customer.dob_input("4 / 20 / 2022")
        time.sleep(5)
        add_customer.input_companyName("DeltaTechnologies")
        add_customer.check_tax_btn()
        add_customer.set_customerRoles("Vendors")
        add_customer.manage_vendor("Vendor 1")
        time.sleep(3)
        add_customer.admin_comment("It's pleasure to have to have you here as a part of Delta Technologies")
        self.logger.info("***************************************Saving added info***********************************")
        add_customer.save_btn()

        details_added_text = self.driver.find_element(By.XPATH,
                                                      '//div[@class="alert alert-success alert-dismissable"]').text
        print(details_added_text)

        if "The new customer has been added successfully." in details_added_text:
            assert True == True
            self.logger.info("**************Customer added successfully************************************")

        else:
            self.driver.save_screenshot(".//Screenshots//", "test_addCustomer.png")  # Screenshot on failure cases
            self.logger.error("*******************Customer adding failed *****************************")
            assert True == False

        self.driver.close()
        self.logger.info("*********************Customer addition test case was successful***********************")
