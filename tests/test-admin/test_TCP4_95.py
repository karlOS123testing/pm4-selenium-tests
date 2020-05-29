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

class TestNewAuthClientRedirectURLField(BaseTest):
    ''' Navigate to the Auth Clients page, create new auth client and test the name input field. '''

    def test_that_new_auth_client_redirect_url_input_field_accepts_long_strings(self):
        ''' Verify that a string 61+ characters long will be accepted in the new auth client name input field.'''
        
        # Login using configured url, workspace, username, and password
        self.driver = login(data['server_url'], data['username'], data['password'], self.driver)

        # Wait for Requests page to load until inner sidebar is displayed
        self.wait.until(EC.visibility_of_element_located((By.ID, 'sidebar-inner')))

        # Click Admin link, wait for Auth Client icon to be clickable to ensure page is loaded 
        self.driver.find_element_by_link_text("Admin").click()
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'fa-key')))

        # Click Auth Clients icon and wait for +Auth Client button to clickable
        self.driver.find_element_by_class_name('fa-key').click()
        self.wait.until(EC.element_to_be_clickable((By.ID, 'create_authclients')))

        # Click +Auth Client button and wait for Enable Authorization Code Grant element on form to be clickable
        self.driver.find_element_by_id('create_authclients').click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Enable Authorization Code Grant')]")))

        # Click Enable Authorization Code Grant element and wait for Redirect URL field to be visible
        self.driver.find_element_by_xpath("//label[contains(text(),'Enable Authorization Code Grant')]").click()
        self.wait.until(EC.visibility_of_element_located((By.ID, 'redirect')))

        # Clear Redirect URL field and verify that long string input works
        long_auth_client_redirect_url = ''.join(random.choice(string.ascii_letters) for n in range(65))
        redirect_url_field = self.driver.find_element_by_id('redirect')
        redirect_url_field.send_keys(long_auth_client_redirect_url)
        self.assertEqual(long_auth_client_redirect_url, redirect_url_field.get_property('value'))


if __name__ == "__main__":
    import __main__
    output = run_test(TestNewAuthClientRedirectURLField, data, __main__)
