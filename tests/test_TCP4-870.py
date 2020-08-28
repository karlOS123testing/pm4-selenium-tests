#!/usr/local/bin/python3

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

###########
class TestLoginUser(BaseTest):

    def setUp(self):
        # Load server url
        self.driver.get(data['server_url'])
 
    def test_correct_login(self):
        '''TCS4_870 Verify the login for an active user'''
        # Load login page.
        login_page = LoginPage(self.driver, data)
        login_page.login()
        # Verify the URL        
        self.assertEqual(self.driver.current_url,data['server_url'] + 'requests')

if __name__ == "__main__":
    import __main__
    output = util.run_test(TestLoginUser, data, __main__)
    print(output)

#########