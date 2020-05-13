#!/usr/local/bin/python3

'''
These lines will run locally, but will not currently work in the Docker image.
They define the path so that imports from parallel folders can be found.

from sys import path
path.append('../')
'''

import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from test_parent import BaseTest
from util import run_test, login

'''
These are in the format necessary when editing the local path.

from includes.test_parent import BaseTest
from includes.util import run_test, login
'''


class TestLogin(BaseTest):
    ''' Test login behaves as expected. '''

    def test_login_designer_page(self):
        ''' Test that user can login and the Designer page displays. '''

        # Login using configured url, workspace, username, and password
        self.driver = login(data['server_url'], data['server_workspace'],
                            data['username'], data['password'], self.driver)

        # Wait for Processes page to load
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.frame_to_be_available_and_switch_to_it("frameMain"))

        # Verify that process grid is displayed
        self.assertTrue(self.driver.find_element_by_id('processesGrid').is_displayed())


if __name__ == "__main__":
    import __main__
    output = run_test(TestLogin, data, __main__)
