#!/usr/local/bin/python3
""" Class to ensure Tablet view Tasks page loads.
"""

# Check if using local environment
from os import getenv

if getenv('ENVIRONMENT') != 'local':
    from test_parent import TabletViewTest
    from util import run_test, login
# If using local environment
else:
    from sys import path
    path.append('../')
    from includes.test_parent import TabletViewTest
    from includes.util import run_test, login
    from __init__ import data

import unittest
import string
import random
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TestTabletViewTasksPageLoads(TabletViewBaseTest):
    ''' Navigate to the Tasks page from Requests page. '''

    def test_that_tablet_view_tasks_page_loads(self):
        ''' Verify that Tasks page loads.'''
        
        # Login using configured url, workspace, username, and password
        self.driver = login(data['server_url'], data['username'], data['password'], self.driver)

        # Wait for Navbar Toggler to be clickable and click
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'navbar-toggler-icon')))
        self.driver.find_element_by_class_name('navbar-toggler-icon').click()

        # Wait for Tasks link to load and click link
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Tasks')))
        self.driver.find_element_by_link_text('Tasks').click()

        # Verify Tasks page elements have loaded
        self.wait.until(EC.visibility_of_element_located((By.ID, 'app-container')))
        self.assertTrue(self.driver.find_element_by_id('sidebar').is_displayed())
        self.assertTrue(self.driver.find_element_by_id('navbar').is_displayed())
        self.assertTrue(self.driver.find_element_by_id('mainbody').is_displayed())
        self.assertTrue(self.driver.find_element_by_id('breadcrumbs').is_displayed())
        self.assertTrue(self.driver.find_element_by_id('tasks').is_displayed())
        self.assertTrue(self.driver.find_element_by_id('search-bar').is_displayed())
        self.assertTrue(self.driver.find_element_by_class_name('data-table').is_displayed())
        

if __name__ == "__main__":
    import __main__
    output = run_test(TestTabletViewTasksPageLoads, data, __main__)
