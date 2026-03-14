import unittest
from selenium import webdriver
from pages.home_page import HomePage


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/index.php")
        self.home_page = HomePage(self.driver)

    def tearDwn(self):
        self.driver.quit()





