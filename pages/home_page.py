from pages.authentication_page import AuthenticationPage
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class Locators:
    """
    Home Page elements locators
    """
    SING_IN_LINK = (By.CLASS_NAME, "login")


class HomePage(BasePage):
    """
    Clicks Sign In and goes to Authentication PAge
    HOME Page Object
    """
    def click_sign_in(self):
        self.driver.find_element(*Locators.SING_IN_LINK).click()
        return AuthenticationPage(self.driver)