#!/usr/local/bin/python3
""" Class to create a new user.
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

class TestNewUserCreated(BaseTest):
    ''' Navigate to the Users page, create new user and verify it is visible. '''

    def test_that_new_user_is_created(self):
        ''' Verify that a new user is successfully created.'''
        
        # Login using configured url, workspace, username, and password
        self.driver = login(data['server_url'], data['username'], data['password'], self.driver)

        # Redirect to Admin Users page, wait for +User button to be clickable 
        self.driver.get(data['server_url'] + '/admin/users')
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-secondary']")))

        # Click +User button and wait for form to load
        self.driver.find_element_by_xpath("//button[@class='btn btn-secondary']").click()
        self.wait.until(EC.visibility_of_element_located((By.ID, 'addUserModal___BV_modal_title_')))

        # Fill out fields
        username = ''.join(random.choice(string.ascii_letters) for n in range(10))
        first_name = ''.join(random.choice(string.ascii_letters) for n in range(10))
        last_name = ''.join(random.choice(string.ascii_letters) for n in range(10))
        job_title = ''.join(random.choice(string.ascii_letters) for n in range(10))
        email = ''.join(random.choice(string.ascii_letters) for n in range(10)) + '@' +\
            ''.join(random.choice(string.ascii_letters) for n in range(10)) + '.' +\
                ''.join(random.choice(string.ascii_letters) for n in range(5))
        password = ''.join(random.choice(string.ascii_letters) for n in range(10))

        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('firstname').send_keys(first_name)
        self.driver.find_element_by_id('lastname').send_keys(last_name)
        self.driver.find_element_by_id('title').send_keys(job_title)
        self.driver.find_element_by_id('email').send_keys(email)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_id('confpassword').send_keys(password)

        # Select options
        Select(self.driver.find_element_by_name("size")).select_by_visible_text("Active")

        # Save and wait for alert to be visible
        self.driver.find_element_by_xpath("//footer[@id='addUserModal___BV_modal_footer_']/button[2]").click()
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'alert')))

        # Save alert, remove leading special characters, and verify text
        alert = (self.driver.find_element_by_class_name('alert').text)[2:]
        self.assertEqual(alert, 'The user was successfully created')


if __name__ == "__main__":
    import __main__
    output = run_test(TestNewUserCreated, data, __main__)
    print(output)