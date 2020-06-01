#!/usr/local/bin/python3
""" Class to test the edit user first name field.
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

class TestEditUserUsernameInputField(BaseTest):
    ''' Navigate to the Users page, edit first user and test the first name input field. '''

    def test_that_edit_user_username_input_field_accepts_long_strings(self):
        ''' Verify that a string 61+ characters long will be accepted in the edit user first name input field.'''
        
        # Login using configured url, workspace, username, and password
        self.driver = login(data['server_url'], data['username'], data['password'], self.driver)

        # Wait for Requests page to load until inner sidebar is displayed
        self.wait.until(EC.visibility_of_element_located((By.ID, 'sidebar-inner')))

        # Click Admin link, wait for Edit User button to be clickable 
        self.driver.find_element_by_link_text("Admin").click()
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'fa-pen-square')))

        # Click Edit User button and wait for form to load
        self.driver.find_element_by_class_name('fa-pen-square').click()
        self.wait.until(EC.visibility_of_element_located((By.ID, 'firstname')))

        # Clear first name field and verify that long string input works
        long_first_name = ''.join(random.choice(string.ascii_letters) for n in range(65))
        first_name_field = self.driver.find_element_by_id('firstname')
        first_name_field.clear()
        first_name_field.send_keys(long_first_name)
        self.assertEqual(long_first_name, first_name_field.get_property('value'))


if __name__ == "__main__":
    import __main__
    output = run_test(TestEditUserUsernameInputField, data, __main__)
