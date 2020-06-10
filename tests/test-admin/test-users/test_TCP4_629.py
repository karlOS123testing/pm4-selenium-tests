#!/usr/local/bin/python3
""" Class to edit a user's permissions. Assign "all permissions".
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

class TestUserAllPermissionsEdited(BaseTest):
    ''' Navigate to the Users page and turn on All Permissions toggle. '''

    def test_that_user_all_permissions_is_edited(self):
        ''' Verify that a user has all permissions assigned.'''
        
        # Login using configured url, workspace, username, and password
        self.driver = login(data['server_url'], data['username'], data['password'], self.driver)

        # Redirect to Admin Edit User ID=2 page, wait for Permissions tab to be clickable 
        self.driver.get(data['server_url'] + '/admin/users/2/edit')
        self.wait.until(EC.element_to_be_clickable((By.ID, 'nav-profile-tab')))
        
        # Click on Permissions tab and wait for it to load
        self.driver.find_element_by_id('nav-profile-tab').click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='selectAll']")))

        # If All Permissions toggle is already selected, turn on 'unselected' bool
        if self.driver.find_element_by_id('selectAll').is_selected():
            unselected = True
        else:
            unselected = False
        
        # Check All Permissions toggle, click save, and wait for alert to show
        self.driver.find_element_by_css_selector("label[for='selectAll']").click()
        self.driver.find_element_by_id('savePermissions').click()
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'alert')))

        # Navigate to Users page and wait for Users table to load and reclick table record edit button
        self.driver.get(data['server_url'] + '/admin/users')
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'vuetable-body')))
        user_tr = self.driver.find_element_by_xpath("//tr//td[1][contains(text(), '2')]").find_element_by_xpath("..")
        user_tr.find_element_by_class_name('fa-pen-square').click()

        # Wait for page to load, click Permissions tab, and wait for Permissions tab to load
        self.wait.until(EC.element_to_be_clickable((By.ID, 'nav-profile-tab')))
        self.driver.find_element_by_id('nav-profile-tab').click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='accordionPermissions']/div[2]/label")))

        # Verify All Permissions toggle is on or off
        if unselected:
            self.assertFalse(self.driver.find_element_by_id('selectAll').is_selected())
        else:
            self.assertTrue(self.driver.find_element_by_id('selectAll').is_selected())


if __name__ == "__main__":
    import __main__
    output = run_test(TestUserAllPermissionsEdited, data, __main__)
