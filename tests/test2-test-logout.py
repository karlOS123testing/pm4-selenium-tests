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


class TestLogout(BaseTest):
    ''' Test logout behaves as expected. '''

    def test_logout(self):
        ''' Test that user can logout and login fields display. '''

        # Login using configured url, workspace, username, and password
        self.driver = login(data['server_url'], data['server_workspace'],
                            data['username'], data['password'], self.driver)

        # Locate logout link and click
        self.driver.find_element_by_link_text('Logout').click()

        # Verify that login page (mep pre-selected) displays
        ''' Note: may want to adapt this to the fqdn link '''
        self.assertTrue(self.driver.find_element_by_id('form[USR_USERNAME]').is_displayed())
        self.assertTrue(self.driver.find_element_by_id('form[USR_PASSWORD_MASK]').is_displayed())
        self.assertTrue(self.driver.find_element_by_id('form[BSUBMIT]').is_displayed())
        self.assertTrue(self.driver.find_element_by_id('page-top').is_displayed())


if __name__ == "__main__":
    import __main__
    output = run_test(TestLogout, data, __main__)
