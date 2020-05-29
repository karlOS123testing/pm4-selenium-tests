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

class TestPasswordRecoveryPageEmailField(BaseTest):
    ''' Navigate to the Forgot Password page and enter text into the email field. '''

    def test_that_forgot_password_page_email_field_accepts_long_strings(self):
        ''' Verify that a string 61+ characters long will be accepted in the password field.'''
        # Navigate to server
        self.driver.get(data['server_url'])

        # Wait for login page to load and click 'Forgot Password?' link
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Forgot Password?')))
        self.driver.find_element_by_link_text('Forgot Password?').click()

        # Create long email address and enter into email field
        long_email = ''.join(random.choice(string.ascii_letters) for n in range(65))
        self.wait.until(EC.visibility_of_element_located((By.ID, 'email')))
        self.driver.find_element_by_id('email').send_keys(long_email)

        # Verify email field contains the long email address
        email_field = self.driver.find_element_by_id('email')
        self.assertEqual(long_email, email_field.get_property('value'))


if __name__ == "__main__":
    import __main__
    output = run_test(TestPasswordRecoveryPageEmailField, data, __main__)