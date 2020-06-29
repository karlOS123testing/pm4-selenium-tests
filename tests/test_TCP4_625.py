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

import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TCP4_625(BaseTest):
    ''' Test that the status of an user can be changed '''

    def test_tcp4_625(self):
        '''Edits an users status'''

        # Login using configured url, workspace, username, and password
        self.driver = login(data['server_url'], data['username'], data['password'], self.driver)

        # Redirect to Admin Users page, wait for +User button to be clickable 
        self.driver.get(data['server_url'] + '/admin/users')
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'vuetable-body')))
        
        # Find table record with ID = '2', find edit button in this element, and click
        user_tr = self.driver.find_element_by_xpath("//tr//td[1][contains(text(), '2')]").find_element_by_xpath("..")
        user_tr.find_element_by_class_name('fa-pen-square').click()
        
        # Wait for user edit form to load, changes the status and save
        self.wait.until(EC.visibility_of_element_located((By.ID, 'firstname')))
        dropdown = Select(self.driver.find_element_by_id('status'))
        dropdown.select_by_index(1)
        self.driver.find_element_by_id('saveUser').click()

        # Navigate to Users page and wait for Users table to load and verify that new name exists for table record 2
        self.driver.get(data['server_url'] + '/admin/users')
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'vuetable-body')))
        user_tr = self.driver.find_element_by_xpath("//tr//td[1][contains(text(), '2')]").find_element_by_xpath("..")
        user_tr.find_element_by_class_name('fa-pen-square').click()

        # Gets the text from the selected option and confirms it changed
        dropdown = Select(self.driver.find_element_by_id('status'))
        option = dropdown.first_selected_option
        self.assertEquals(option.text, 'INACTIVE')

if __name__ == "__main__":
    import __main__  
    output = run_test(TCP4_625, data, __main__)