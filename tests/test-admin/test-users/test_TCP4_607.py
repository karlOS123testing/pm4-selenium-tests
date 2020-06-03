#!/usr/local/bin/python3
""" Class to edit a user's first name.
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

class TestUserFirstNameEdited(BaseTest):
    ''' Navigate to the Users page and edit a user's first name. '''

    def test_that_user_first_name_is_edited(self):
        ''' Verify that a user's first name is successfully edited.'''
        
        # Login using configured url, workspace, username, and password
        self.driver = login(data['server_url'], data['username'], data['password'], self.driver)

        # Redirect to Admin Users page, wait for +User button to be clickable 
        self.driver.get(data['server_url'] + '/admin/users')
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'vuetable-body')))
        
        # Find table record with ID = '2', find edit button in this element, and click
        user_tr = self.driver.find_element_by_xpath("//tr//td[1][contains(text(), '2')]").find_element_by_xpath("..")
        user_tr.find_element_by_class_name('fa-pen-square').click()
        
        # Wait for user edit form to load, change first name, and save
        self.wait.until(EC.visibility_of_element_located((By.ID, 'firstname')))
        self.driver.find_element_by_id('firstname').clear()
        first_name = ''.join(random.choice(string.ascii_letters) for n in range(10))
        self.driver.find_element_by_id('firstname').send_keys(first_name)
        self.driver.find_element_by_id('saveUser').click()

        # Navigate to Users page and wait for Users table to load and verify that new name exists for table record 2
        self.driver.get(data['server_url'] + '/admin/users')
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'vuetable-body')))
        user_tr = self.driver.find_element_by_xpath("//tr//td[1][contains(text(), '2')]").find_element_by_xpath("..")
        self.assertTrue(user_tr.find_element_by_xpath(".//td[contains(text(), " + first_name + ")]"))


if __name__ == "__main__":
    import __main__
    output = run_test(TestUserFirstNameEdited, data, __main__)

