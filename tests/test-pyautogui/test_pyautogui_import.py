#!/usr/local/bin/python3
""" Class to test the new auth client name field.
"""

# Check if using local environment
from os import getenv

if getenv('ENVIRONMENT') == 'docker':
    from test_parent import BaseTest
    from util import run_test, login
# If using local environment
else:
    from sys import path
    path.append('../')
    from includes.test_parent import BaseTest
    from includes.util import run_test, login
    from __init__ import data

import pyautogui
import unittest
import string
import random
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TestPyautoguiImport(BaseTest):
    ''' Navigate to the Requests page. '''

    def test_that_import_works(self):
        ''' Verify that pyautogui import doesn't cause test to fail.'''
        
        # Login using configured url, workspace, username, and password
        self.driver = login(data['server_url'], data['username'], data['password'], self.driver)

        # Wait for Requests page to load until inner sidebar is displayed and assert it is
        self.wait.until(EC.visibility_of_element_located((By.ID, 'sidebar-inner')))
        self.assertTrue(self.driver.find_element_by_id('sidebar-inner').is_displayed())


if __name__ == "__main__":
    import __main__
    output = run_test(TestPyautoguiImport, data, __main__)
    