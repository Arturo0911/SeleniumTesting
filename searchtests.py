#!/usr/bin/python3

import unittest
from selenium import webdriver

class HomePageTests(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")

        # indicate to maximize, bacause there may be responsive elements
        driver.maximize_window()
        
        # to set a pause
        self.driver.implicitly_wait(15)


    def test_search_text_field(self):
        
        # to see the fiel search
        search_field = self.driver.find_element_by_id("search")

    def tearDown(self) -> None:
        # close windows and any sessions activated
        self.driver.quit()



if __name__ == "__main__":
    unittest.main(verbosity=2)

