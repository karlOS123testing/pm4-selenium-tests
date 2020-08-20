#!/usr/local/bin/python3

# Check if using local environment
from os import getenv

if getenv('ENVIRONMENT') != 'local':
    from test_parent import BaseTest
    from util import run_test

    
# If using local environment
else:
    from sys import path
    path.append('../')
    from includes.test_parent import BaseTest
    from includes.util import run_test
    from __init__ import data
    from includes.page_login import PageLogin
    from includes.page_menu import PageMenu
    from includes.page_user import PageUsers

import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TCP4_2(BaseTest):
    ''' Test that the username field at login accepts a 60 character string '''

    def test_tcp4_2(self):
        '''write a 60 character string on the username field'''

        # Login using configured url, workspace, username, and password
        self.driver = PageLogin(self.driver, data).login()

        # Log out
        PageMenu(self.driver, data).log_out()

        # Insert a 60 characters string on the username field
        self.assertTrue(PageLogin(self.driver, data).user_long_string())

if __name__ == "__main__":
    import __main__
    output = run_test(TCP4_2, data, __main__)
    print(output)