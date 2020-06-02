#!/usr/local/bin/python3
""" Class to test the new group name field.
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

class TestNewGroupNameInputField(BaseTest):
    ''' Navigate to the Add New Group form and test the name input field. '''

    def test_that_new_group_name_field_accepts_long_strings(self):
        ''' Verify that a string 61+ characters long will be accepted in the group name field.'''
        
        # Login using configured url, workspace, username, and password
        self.driver = login(data['server_url'], data['username'], data['password'], self.driver)

        # Wait for Requests page to load until inner sidebar is displayed
        self.wait.until(EC.visibility_of_element_located((By.ID, 'sidebar-inner')))

        # Click Admin link, wait for Groups icon to be clickable to ensure page is loaded 
        self.driver.find_element_by_link_text("Admin").click()
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'fa-users')))

        # Click Groups icon and wait for +Group button to be clickable
        self.driver.find_element_by_class_name('fa-users').click()
        self.wait.until(EC.element_to_be_clickable((By.ID, 'create_group')))

        # Click +Group button and wait for form to load
        self.driver.find_element_by_id('create_group').click()
        self.wait.until(EC.visibility_of_element_located((By.ID, 'name')))


        # Create long group name and verify user can enter a long group name into name input field
        long_group_name = ''.join(random.choice(string.ascii_letters) for n in range(65))
        self.driver.find_element_by_id('name').send_keys(long_group_name)
        name_field = self.driver.find_element_by_id('name')
        self.assertEqual(long_group_name, name_field.get_property('value'))


if __name__ == "__main__":
    import __main__
    output = run_test(TestNewGroupNameInputField, data, __main__)