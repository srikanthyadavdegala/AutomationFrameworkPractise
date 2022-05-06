import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer:
    """Adding Customers"""
    lnk_customers_menu_xpath = '//a[@href="#"]/child::p[contains(text(),"Customers")]'
    lnk_customers_menuitem_xpath = "//a[@href='/Admin/Customer/List']/child::p[text()=' Customers']"
    btn_addNew_xpath = '//a[@href="/Admin/Customer/Create"]'

    txt_email_id = 'Email'
    txt_passwd_id = 'Password'
    txt_firstName_id = 'FirstName'
    txt_lastName_id = 'LastName'

    radio_genderMale_id = 'Gender_Male'
    radio_genderFemale_id = 'Gender_Female'
    txt_dob_xpath = "//input[@id='DateOfBirth']"
    txt_companyName_id = 'Company'
    chkBox_tax_id = 'IsTaxExempt'

    customer_role_box_xpath = '//li[@role="option"]//span[text()="Registered"]'
    option_registered_del_xpath = '//span[@title= "delete"]'
    select_guest_xpath = '//li[text()= "Guests"]'
    select_registered_xpath = '//li[text()= "Registered"]'
    select_administrator_xpath = '//li[text()= "Administrators"]'
    select_formModerators_xpath = '//li[text()= "Forum Moderators"]'
    select_vendor_xpath = '//li[text()= "Vendors"]'

    manage_vendor_id = "VendorId"
    txt_adminComment_id = 'AdminComment'
    btn_save_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def click_customersMenu(self):
        self.driver.find_element(By.XPATH, self.lnk_customers_menu_xpath).click()

    def click_customerMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnk_customers_menuitem_xpath).click()

    def click_AddNewButton(self):
        self.driver.find_element(By.XPATH, self.btn_addNew_xpath).click()

    def input_email(self, input_email):
        self.driver.find_element(By.ID, self.txt_email_id).clear()
        self.driver.find_element(By.ID, self.txt_email_id).send_keys(input_email)

    def input_password(self, input_password):
        self.driver.find_element(By.ID, self.txt_passwd_id).clear()
        self.driver.find_element(By.ID, self.txt_passwd_id).send_keys(input_password)

    def input_FirstName(self, input_fname):
        self.driver.find_element(By.ID, self.txt_firstName_id).clear()
        self.driver.find_element(By.ID, self.txt_firstName_id).send_keys(input_fname)

    def input_LastName(self, input_Lname):
        self.driver.find_element(By.ID, self.txt_lastName_id).clear()
        self.driver.find_element(By.ID, self.txt_lastName_id).send_keys(input_Lname)

    def set_gender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.ID, self.radio_genderMale_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID, self.radio_genderFemale_id).click()
        else:
            self.driver.find_element(By.ID, self.radio_genderMale_id).click()

    def dob_input(self, dob):
        self.driver.find_element(By.XPATH, self.txt_dob_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_dob_xpath).send_keys(dob)

    def input_companyName(self, company_Name):
        self.driver.find_element(By.ID, self.txt_companyName_id).clear()
        self.driver.find_element(By.ID, self.txt_companyName_id).send_keys(company_Name)

    def check_tax_btn(self):
        tax_btn = self.driver.find_element(By.ID, self.chkBox_tax_id)
        tax_btn.click()

    def set_customerRoles(self, role):
        self.driver.find_element(By.XPATH, self.customer_role_box_xpath).click()
        time.sleep(3)
        if role == "Registered":
            self.list_value = self.driver.find_element(By.XPATH, self.select_registered_xpath)
        elif role == "Administrators":
            self.list_value = self.driver.find_element(By.XPATH, self.select_administrator_xpath)
        elif role == "Forum Moderators":
            self.list_value = self.driver.find_element(By.XPATH, self.select_formModerators_xpath)
        elif role == "Vendors":
            self.list_value = self.driver.find_element(By.XPATH, self.select_vendor_xpath)
        elif role == "Guests":
            time.sleep(5)
            """Either can be Guest or Registered Customer, so Registered role should be deleted prior"""
            self.driver.find_element(By.XPATH, self.option_registered_del_xpath).click()
            self.list_value = self.driver.find_element(By.XPATH, self.select_guest_xpath)

        else:
            self.list_value = self.driver.find_element(By.XPATH, self.select_guest_xpath)

        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", self.list_value)

    def manage_vendor(self, value):
        select_option = Select(self.driver.find_element(By.ID, self.manage_vendor_id))
        select_option.select_by_visible_text(value)

    def admin_comment(self, comment):
        self.driver.find_element(By.ID, self.txt_adminComment_id).clear()
        self.driver.find_element(By.ID, self.txt_adminComment_id).send_keys(comment)

    def save_btn(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()
