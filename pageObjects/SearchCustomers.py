import time

from selenium.webdriver.common.by import By


class SearchCustomerData:
    search_email_xpath = "//input[@name='SearchEmail']"
    search_fname_xpath = "//input[@id='SearchFirstName']"
    search_lname_xpath = "//input[@id='SearchLastName']"
    btn_search_xpath = "//button[@id='search-customers']"
    table_xpath = "//div[@id='customers-grid_wrapper']//div[@class='dataTables_scroll']"

    table_data_xpath = "//div[@class='dataTables_scrollBody']"
    table_rowData_xpath = "//div[@class='dataTables_scrollBody']//tbody/tr"
    table_columnData_xpath = "//div[@class='dataTables_scrollBody']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def search_email(self, email):
        self.driver.find_element(By.XPATH, self.search_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.search_email_xpath).send_keys(email)

    def search_firstname(self, firstname):
        self.driver.find_element(By.XPATH, self.search_fname_xpath).clear()
        self.driver.find_element(By.XPATH, self.search_fname_xpath).send_keys(firstname)

    def search_lastname(self, lastname):
        self.driver.find_element(By.XPATH, self.search_lname_xpath).clear()
        self.driver.find_element(By.XPATH, self.search_lname_xpath).send_keys(lastname)

    def search_btn(self):
        self.driver.find_element(By.XPATH, self.btn_search_xpath).click()

    def table_rowCount(self):
        return len(self.driver.find_elements(By.XPATH, self.table_rowData_xpath))

    def table_columnCount(self):
        return len(self.driver.find_elements(By.XPATH, self.table_columnData_xpath))

    def customerSearchEmail(self, email):
        Flag = False
        for r in range(1, self.table_rowCount() + 1):
            table = self.driver.find_element(By.XPATH, self.table_data_xpath)
            email_id = self.driver.find_element(By.XPATH,
                                                "//div[@class='dataTables_scrollBody']//tbody/tr[" + str(
                                                    r) + "]/td[2]").text
            if email == email_id:
                Flag = True
                break
        return Flag

    def customerSearchName(self, name):
        Flag = False
        for r in range(1, self.table_rowCount() + 1):
            Name = self.driver.find_element(By.XPATH, "//div[@class='dataTables_scrollBody']//tbody/tr[" + str(
                r) + "]/td[3]").text
            if name == Name:
                Flag = True
                break
        return Flag
