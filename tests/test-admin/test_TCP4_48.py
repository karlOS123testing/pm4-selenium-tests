#!/usr/local/bin/python3
""" Class to test the user search text field.
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

class TestLoginPageUsernameField(BaseTest):
    ''' Navigate to the login page and enter text into the username field. '''

    def test_that_login_username_field_accepts_long_strings(self):
        ''' Verify that a string 61+ characters long will be accepted in the username field.'''
        # Navigate to server
        self.driver.get(data['server_url'])

        # Wait for login page to load
        self.wait.until(EC.element_to_be_clickable((By.NAME, 'username')))

        # Create long user name and enter into username field
        long_user_name = ''.join(random.choice(string.ascii_letters) for n in range(65))
        self.driver.find_element_by_id('username').send_keys(long_user_name)

        # Verify username field contains the long user name
        username_field = self.driver.find_element_by_id('username')
        self.assertEqual(long_user_name, username_field.get_property('value'))


if __name__ == "__main__":
    import __main__
    output = run_test(TestLoginPageUsernameField, data, __main__)