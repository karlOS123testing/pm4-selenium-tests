#Paths used on POM_POC

#!/usr/local/bin/python3

# Check if using local environment
from os import getenv

if getenv('ENVIRONMENT') != 'local':
    from test_parent import BaseTest

import unittest
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class POC(BaseTest):
    def path_POM_POC(self):
        user_search_bar = self.driver.find_element_by_css_selector("input[class='form-control']").find_element_by_xpath("..")
        self.wait.until(EC.visibility_of(user_search_bar))