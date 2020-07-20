#!/usr/local/bin/python3
# functions for the POM POC
from os import getenv

if getenv('ENVIRONMENT') != 'local':
    from test_parent import BaseTest
    
# If using local environment
else:
    from sys import path
    path.append('../')
    from includes.test_parent import BaseTest

import unittest
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class file_menu(BaseTest):

    def goto_admin(self, driver, data):
        # Go to the admin tab
        self.driver.get(data['server_url'] + '/admin/users')
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "form-control")))