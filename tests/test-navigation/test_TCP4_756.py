#!/usr/local/bin/python3
""" Class to ensure Script Executors page loads.
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

class TestScriptExecutorsPageLoads(BaseTest):
    ''' Navigate to the Script Executors page from Admin page. '''

    def test_that_script_executors_page_loads(self):
        ''' Verify that Script Executors page loads.'''
        
        # Login using configured url, workspace, username, and password
        self.driver = login(data['server_url'], data['username'], data['password'], self.driver)

        # Navigate to Admin page
        self.driver.get(data['server_url'] + '/admin/users')

        # Wait for Script Executors button to be clickable and click button
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class='fas nav-icon fa-code']")))
        self.driver.find_element_by_xpath("//i[@class='fas nav-icon fa-code']").click()

        # Verify Script Executors page elements have loaded
        self.wait.until(EC.visibility_of_element_located((By.ID, 'app-container')))
        self.assertTrue(self.driver.find_element_by_id('sidebar').is_displayed())
        self.assertTrue(self.driver.find_element_by_id('navbar').is_displayed())
        self.assertTrue(self.driver.find_element_by_id('mainbody').is_displayed())
        self.assertTrue(self.driver.find_element_by_id('breadcrumbs').is_displayed())
        self.assertTrue(self.driver.find_element_by_id('script-executors').is_displayed())
        self.assertTrue(self.driver.find_element_by_id('__BVID__45').is_displayed())
        self.assertTrue(self.driver.find_element_by_class_name('d-flex').is_displayed())


if __name__ == "__main__":
    import __main__
    output = run_test(TestScriptExecutorsPageLoads, data, __main__)
