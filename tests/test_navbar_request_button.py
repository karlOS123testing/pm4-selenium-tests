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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TestNavbarRequestButton(BaseTest):
    ''' Navigate to the Admin page. '''

    def test_navbar_request_button(self):
        ''' Test that navbar request button displays on Admin page. '''

        # Login using configured url, workspace, username, and password
        self.driver = login(data['server_url'], data['username'], data['password'], self.driver)

        # Wait for Requests page to load until inner sidebar is displayed
        self.wait.until(EC.visibility_of_element_located((By.ID, 'sidebar-inner')))

        # Click Admin link, wait for +request button to appear to ensure page is loaded 
        self.driver.find_element_by_link_text("Admin").click()
        self.wait.until(EC.visibility_of_element_located((By.ID, 'navbar-request-button')))
        self.assertTrue(self.driver.find_element_by_id('navbar-request-button').is_displayed())

        
if __name__ == "__main__":
    import __main__
    output = run_test(TestNavbarRequestButton, data, __main__)
