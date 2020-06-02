#!/usr/local/bin/python3
""" Class to test the groups search text field.
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

class TestGroupSearchBarInputField(BaseTest):
    ''' Navigate to the Groups page and test the search bar field. '''

    def test_that_group_search_bar_field_accepts_long_strings(self):
        ''' Verify that a string 61+ characters long will be accepted in the group search bar field.'''
        
        # Login using configured url, workspace, username, and password
        self.driver = login(data['server_url'], data['username'], data['password'], self.driver)

        # Wait for Requests page to load until inner sidebar is displayed
        self.wait.until(EC.visibility_of_element_located((By.ID, 'sidebar-inner')))

        # Click Admin link, wait for Groups icon to be clickable to ensure page is loaded 
        self.driver.find_element_by_link_text("Admin").click()
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'fa-users')))

        # Click Groups icon and wait for search bar field to visible
        self.driver.find_element_by_class_name('fa-users').click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search']")))

        # Create long group name and verify user can enter a long group name into name input field
        long_group_search = ''.join(random.choice(string.ascii_letters) for n in range(65))
        self.driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys(long_group_search)
        search_field = self.driver.find_element_by_xpath("//input[@placeholder='Search']")
        self.assertEqual(long_group_search, search_field.get_property('value'))


if __name__ == "__main__":
    import __main__
    output = run_test(TestGroupSearchBarInputField, data, __main__)