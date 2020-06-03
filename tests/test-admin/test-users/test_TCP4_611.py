#!/usr/local/bin/python3
""" Class to edit a user's phone.
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

class TestUserPhoneEdited(BaseTest):
    ''' Navigate to the Users page and edit a user's phone. '''

    def test_that_user_phone_is_edited(self):
        ''' Verify that a user's phone is successfully edited.'''
        
        # Login using configured url, workspace, username, and password
        self.driver = login(data['server_url'], data['username'], data['password'], self.driver)

        # Redirect to Admin Users page, wait for +User button to be clickable 
        self.driver.get(data['server_url'] + '/admin/users')
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'vuetable-body')))
        
        # Find table record with ID = '2', find edit button in this element, and click
        user_tr = self.driver.find_element_by_xpath("//tr//td[1][contains(text(), '2')]").find_element_by_xpath("..")
        user_tr.find_element_by_class_name('fa-pen-square').click()
        
        # Wait for user edit form to load, change phone, and save
        self.wait.until(EC.visibility_of_element_located((By.ID, 'phone')))
        self.driver.find_element_by_id('phone').clear()
        phone = ''.join(random.choice(string.ascii_letters) for n in range(10)) + '@' +\
            ''.join(random.choice(string.ascii_letters) for n in range(10)) + '.' +\
                ''.join(random.choice(string.ascii_letters) for n in range(5))
        self.driver.find_element_by_id('phone').send_keys(phone)
        self.driver.find_element_by_id('saveUser').click()

        # Navigate to Users page and wait for Users table to load and reclick table record edit button
        self.driver.get(data['server_url'] + '/admin/users')
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'vuetable-body')))
        user_tr = self.driver.find_element_by_xpath("//tr//td[1][contains(text(), '2')]").find_element_by_xpath("..")
        user_tr.find_element_by_class_name('fa-pen-square').click()

        # Wait for edit user form to load and verify phone field contains correct phone
        self.wait.until(EC.visibility_of_element_located((By.ID, 'phone')))
        phone_field = self.driver.find_element_by_id('phone')
        self.assertEqual(phone_field.get_property('value'), phone)


if __name__ == "__main__":
    import __main__
    output = run_test(TestUserPhoneEdited, data, __main__)
