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

class TestUserSearchField(BaseTest):
    ''' Navigate to the Admin/Users page and enter text into the Search bar. '''

    def test_that_user_search_field_accepts_long_strings(self):
        ''' Verify that a string 61+ characters long will be accepted in the User Search bar.'''
        # Login using configured url, workspace, username, and password
        self.driver = login(data['server_url'], data['username'], data['password'], self.driver)

        # Wait for Requests page to load until inner sidebar is displayed
        self.wait.until(EC.visibility_of_element_located((By.ID, 'sidebar-inner')))

        # Click Admin link, wait for +request button to appear to ensure page is loaded 
        self.driver.find_element_by_link_text("Admin").click()
        self.wait.until(EC.visibility_of_element_located((By.ID, 'nav-users-tab')))

        # Create long user name and enter into Search bar
        long_user_name = ''.join(random.choice(string.ascii_letters) for n in range(65))
        self.driver.find_element_by_xpath("//div[@id='users-listing']//input[@placeholder='Search']").send_keys(long_user_name)

        # Verify Search bar contains the long user name
        search_bar_text = self.driver.find_element_by_xpath("//div[@id='users-listing']//input[@placeholder='Search']")
        self.assertEqual(long_user_name, search_bar_text.get_property('value'))


if __name__ == "__main__":
    import __main__
    output = run_test(TestUserSearchField, data, __main__)