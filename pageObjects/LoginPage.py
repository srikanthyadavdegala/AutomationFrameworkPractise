from selenium.webdriver.common.by import By


class Login:
    textbox_email_id = "Email"
    textbox_password_xpath = "//input[@name='Password']"
    button_login_xpath = '//button[text()="Log in"]'
    link_logout_xpath = "//a[@href='/logout']"

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element(By.ID, self.textbox_email_id).clear()
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def login(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def logout(self):
        self.driver.find_element(By.XPATH, self.link_logout_xpath).click()
