#!/usr/local/bin/python3
""" Class to test the login page username field.
"""

# Check if using local environment
from os import getenv, path
if getenv('ENVIRONMENT') == 'local':
    from sys import path
    path.append('../includes')
    from __init__ import data

from test_parent import BaseTest
import util
from page import *
import unittest


class TestLoginPageUsernameField(BaseTest):
    ''' Navigate to the login page and enter text into the username field. '''

    def setUp(self):
        # Load server url
        self.driver.get(data['server_url'])

    def test_that_login_username_field_accepts_long_strings(self):
        ''' Verify that a string 61+ characters long will be accepted in the username field.'''
        # Load login page.
        login_page = LoginPage(self.driver, data)

        # Check if browser is at login page
        self.assertTrue(login_page.is_url_matches())

        # Enter long string in username field
        long_username = util.generate_long_text()
        login_page.username_field_element = long_username

        self.assertEqual(login_page.username_field_element, long_username)


if __name__ == "__main__":
    import __main__
    output = util.run_test(TestLoginPageUsernameField, data, __main__)
