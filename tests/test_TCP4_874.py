#!/usr/local/bin/python3
""" Class to test the login page username field.
"""

# Check if using local environment
from os import getenv, path
#if getenv('ENVIRONMENT') == 'local':
from sys import path
path.append('../includes')
from __init__ import data
from test_parent import BaseTest
import util
from page import *
import unittest


class Test_TCP4_874(BaseTest):
    ''' Verify the login for an inactive user '''

    def setUp(self):
        # Load server url
        self.driver.get(data['server_url'])

    def testInactiveUser(self):
        # Load login page.
        login_page = LoginPage(self.driver, data)
        login_page.login()

        # Verify the URL
        self.assertEqual(self.driver.current_url,data['server_url'] + 'login')


if __name__ == "__main__":
    import __main__
    output = util.run_test(Test_TCP4_874, data, __main__)
    print(output)