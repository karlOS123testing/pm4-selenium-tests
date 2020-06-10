#!/usr/local/bin/python3
""" Class to ensure Documentation page loads.
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

class TestDocumentationPageLoads(BaseTest):
    ''' Navigate to the Documentation page from Admin page. '''

    def test_that_documentation_page_loads(self):
        ''' Verify that Documentation page loads.'''
        
        # Login using configured url, workspace, username, and password
        self.driver = login(data['server_url'], data['username'], data['password'], self.driver)

        # Wait for avatar button to be clickable and click button
        self.wait.until(EC.element_to_be_clickable((By.ID, 'avatarMenu')))
        self.driver.find_element_by_id('avatarMenu').click()

        # Wait for Documentation button to be clickable and click button
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Documentation')))
        self.driver.find_element_by_link_text('Documentation').click()

        # Switch to new tab
        self.driver.switch_to.window(self.driver.window_handles[1])

        # Verify Documentation page elements have loaded
        self.wait.until(EC.visibility_of_element_located((By.ID, '__GITBOOK__ROOT__CLIENT__')))
        self.assertEqual(self.driver.current_url, 'https://processmaker.gitbook.io/processmaker/')


if __name__ == "__main__":
    import __main__
    output = run_test(TestDocumentationPageLoads, data, __main__)
