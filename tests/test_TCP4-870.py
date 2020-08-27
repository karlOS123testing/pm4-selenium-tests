#!/usr/local/bin/python3

# Check if using local environment

from os import getenv, path
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
        ''' Verify the login for an active user'''
        # Load login page.
        login_page = LoginPage(self.driver, data)
        login_page.login()
        
        urlUser = self.driver.current_url
        #print('1 - urlUser: '+urlUser+'**')

        self.assertEqual(urlUser,'https://release-testing.processmaker.net/requests')

if __name__ == "__main__":
    import __main__
    output = util.run_test(TestLoginUser, data, __main__)
    print(output)

#########