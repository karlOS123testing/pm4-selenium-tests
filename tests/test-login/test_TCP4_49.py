#!/usr/local/bin/python3
""" Class to test the login page password field.
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

class TestLoginPagePasswordField(BaseTest):
    ''' Navigate to the login page and enter text into the password field. '''

    def test_that_login_password_field_accepts_long_strings(self):
        ''' Verify that a string 61+ characters long will be accepted in the password field.'''
        # Navigate to server
        self.driver.get(data['server_url'])

        # Wait for login page to load
        self.wait.until(EC.element_to_be_clickable((By.NAME, 'password')))

        # Create long user name and enter into username field
        long_user_name = ''.join(random.choice(string.ascii_letters) for n in range(65))
        self.driver.find_element_by_id('password').send_keys(long_user_name)

        # Verify username field contains the long user name
        password_field = self.driver.find_element_by_id('password')
        self.assertEqual(long_user_name, password_field.get_property('value'))


if __name__ == "__main__":
    import __main__
    output = run_test(TestLoginPagePasswordField, data, __main__)