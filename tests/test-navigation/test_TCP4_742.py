#!/usr/local/bin/python3
""" Class to ensure Tablet view Designer page loads.
"""

# Check if using local environment
from os import getenv

if getenv('ENVIRONMENT') != 'local':
    from test_parent import TabletViewBaseTest
    from util import run_test, login
# If using local environment
else:
    from sys import path
    path.append('../')
    from includes.test_parent import TabletViewBaseTest
    from includes.util import run_test, login
    from __init__ import data

import unittest
import string
import random
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TestTabletViewDesignerPageLoads(TabletViewBaseTest):
    ''' Navigate to the Designer page from Requests page. '''

    def test_that_tablet_view_designer_page_loads(self):
        ''' Verify that Designer page loads.'''
        
        # Login using configured url, workspace, username, and password
        self.driver = login(data['server_url'], data['username'], data['password'], self.driver)

        # Wait for Navbar Toggler to be clickable and click
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'navbar-toggler-icon')))
        self.driver.find_element_by_class_name('navbar-toggler-icon').click()

        # Wait for Designer link to load and click link
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Designer')))
        self.driver.find_element_by_link_text('Designer').click()

        # Verify Designer page elements have loaded
        self.wait.until(EC.visibility_of_element_located((By.ID, 'app-container')))
        self.assertTrue(self.driver.find_element_by_id('sidebar').is_displayed())
        self.assertTrue(self.driver.find_element_by_id('navbar').is_displayed())
        self.assertTrue(self.driver.find_element_by_id('mainbody').is_displayed())
        self.assertTrue(self.driver.find_element_by_id('breadcrumbs').is_displayed())
        self.assertTrue(self.driver.find_element_by_id('categorizedList').is_displayed())
        self.assertTrue(self.driver.find_element_by_id('nav-sources-tab').is_displayed())
        self.assertTrue(self.driver.find_element_by_id('nav-categories-tab').is_displayed())
        self.assertTrue(self.driver.find_element_by_id('nav-archived-tab').is_displayed())
        self.assertTrue(self.driver.find_element_by_id('nav-sources').is_displayed())
        

if __name__ == "__main__":
    import __main__
    output = run_test(TestTabletViewDesignerPageLoads, data, __main__)
