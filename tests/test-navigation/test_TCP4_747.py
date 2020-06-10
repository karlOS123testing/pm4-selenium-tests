#!/usr/local/bin/python3
""" Class to ensure Tasks Completed page loads.
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

class TestTasksCompletedPageLoads(BaseTest):
    ''' Navigate to the Tasks Completed page from Requests page. '''

    def test_that_tasks_completed_page_loads(self):
        ''' Verify that Tasks Completed page loads.'''
        
        # Login using configured url, workspace, username, and password
        self.driver = login(data['server_url'], data['username'], data['password'], self.driver)

        # Navigate to Tasks page
        self.driver.get(data['server_url'] + '/tasks')

        # Wait for Tasks Completed button to be clickable and click button
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class='fas nav-icon fa-check-square']")))
        self.driver.find_element_by_xpath("//i[@class='fas nav-icon fa-check-square']").click()

        # Verify Tasks Completed page elements have loaded
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
    output = run_test(TestTasksCompletedPageLoads, data, __main__)