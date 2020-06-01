#!/usr/local/bin/python3
""" Class to test the edit auth name field.
"""

# Check if using local environment
from os import getenv

if getenv('ENVIRONMENT') != 'local':
    from test_parent import BaseTest
    from util import run_test, login
# If using local environment
else:
    from sys import path
    path.append('../')
    from includes.test_parent import BaseTest
    from includes.util import run_test, login
    from __init__ import data

import unittest
import string
import random
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TestEditAuthClientNameInputField(BaseTest):
    ''' Navigate to the Auth Clients page, edit an auth client and test the name input field. '''

    def test_that_new_auth_client_name_input_field_accepts_long_strings(self):
        ''' Verify that a string 61+ characters long will be accepted in the edit auth client name input field.'''
        
        # Login using configured url, workspace, username, and password
        self.driver = login(data['server_url'], data['username'], data['password'], self.driver)

        # Wait for Requests page to load until inner sidebar is displayed
        self.wait.until(EC.visibility_of_element_located((By.ID, 'sidebar-inner')))

        # Click Admin link, wait for Auth Client icon to be clickable to ensure page is loaded 
        self.driver.find_element_by_link_text("Admin").click()
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'fa-key')))

        # Click Auth Clients icon and wait for Edit Auth Client button to clickable
        self.driver.find_element_by_class_name('fa-key').click()
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'fa-pen-square')))

        # Click Edit Auth Client button and wait for name element on form to be visible
        self.driver.find_element_by_class_name('fa-pen-square').click()
        self.wait.until(EC.visibility_of_element_located((By.ID, 'name')))

        # Clear name field verify that long string input works
        long_auth_client_name = ''.join(random.choice(string.ascii_letters) for n in range(65))
        name_field = self.driver.find_element_by_id('name')
        name_field.clear()
        name_field.send_keys(long_auth_client_name)
        self.assertEqual(long_auth_client_name, name_field.get_property('value'))


if __name__ == "__main__":
    import __main__
    output = run_test(TestEditAuthClientNameInputField, data, __main__)
