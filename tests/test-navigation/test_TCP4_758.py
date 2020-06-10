#!/usr/local/bin/python3
""" Class to ensure Edit admin Profile page loads.
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

class TestEditAdminProfilePageLoads(BaseTest):
    ''' Navigate to the Edit admin Profile page from Admin page. '''

    def test_that_edit_admin_profile_page_loads(self):
        ''' Verify that Edit admin Profile page loads.'''
        
        # Login using configured url, workspace, username, and password
        self.driver = login(data['server_url'], data['username'], data['password'], self.driver)

        # Wait for avatar button to be clickable and click button
        self.wait.until(EC.element_to_be_clickable((By.ID, 'avatarMenu')))
        self.driver.find_element_by_id('avatarMenu').click()

        # Wait for Edit admin Profile button to be clickable and click button
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Edit admin Profile')))
        self.driver.find_element_by_link_text('Edit admin Profile').click()

        # Verify Edit admin Profile page elements have loaded
        self.wait.until(EC.visibility_of_element_located((By.ID, 'app-container')))
        self.assertTrue(self.driver.find_element_by_id('sidebar').is_displayed())
        self.assertTrue(self.driver.find_element_by_id('navbar').is_displayed())
        self.assertTrue(self.driver.find_element_by_id('mainbody').is_displayed())
        self.assertTrue(self.driver.find_element_by_id('breadcrumbs').is_displayed())
        self.assertTrue(self.driver.find_element_by_id('profileForm').is_displayed())


if __name__ == "__main__":
    import __main__
    output = run_test(TestEditAdminProfilePageLoads, data, __main__)
