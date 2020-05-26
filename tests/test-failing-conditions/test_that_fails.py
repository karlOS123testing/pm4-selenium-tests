#!/usr/local/bin/python3

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
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TestSidebarDisplayed(BaseTest):
    ''' Test that sidebar is displayed on Requests page. '''

    def test_sidebar_displayed(self):
        ''' Verify sidebar is displayed. '''

        # Login using configured url, workspace, username, and password
        self.driver = login(data['server_url'], data['username'], data['password'], self.driver)

        # Wait for Requests page to load, verify that inner sidebar is displayed
        self.wait.until(EC.visibility_of_element_located((By.ID, 'sidebar-inner')))
        self.assertFalse(self.driver.find_element_by_id('sidebar-inner').is_displayed())
        

if __name__ == "__main__":
    import __main__
    output = run_test(TestSidebarDisplayed, data, __main__)
