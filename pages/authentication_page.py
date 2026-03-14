from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class Locators:

    """
    Authentication page locators
    """
    CREATE_ACCOUNT_EMAIL = (By.ID,"email_crete")

class AuthenticationPage(BasePage):

    """
    Authentication Page Object
    """
    def enter_create_account(self, email):
        """
        Enter email for new user registration
        :param email:
        :return:
        """
        self.driver.find_element_by_id(*Locators.CREATE_ACCOUNT_EMAIL).send_keys(email)
        pass