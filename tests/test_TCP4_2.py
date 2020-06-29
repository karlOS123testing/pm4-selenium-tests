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

class TCP4_2(BaseTest):
    ''' Test that the username field at login accepts a 60 character string '''

    def test_tcp4_2(self):
        '''write a 60 character string on the username field'''

        # Login using configured url, workspace, username, and password
        self.driver = login(data['server_url'], data['username'], data['password'], self.driver)

        # Log out
        self.wait.until(EC.visibility_of_element_located((By.ID, 'avatarMenu')))
        self.driver.find_element_by_id("avatarMenu").click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "li>a[href='/logout']")))
        self.driver.find_element_by_css_selector("li>a[href='/logout']").click()

        # Insert a 60 characters string on the username field
        self.wait.until(EC.visibility_of_element_located((By.ID, 'username')))

        self.driver.find_element_by_id("username").send_keys('qwertyuiopasdfghjklñzxcvbnmqwertyuiopasdfghjklñzxcvbnmqwerty')
        self.assertEquals(self.driver.find_element_by_id("username").get_property('value'), 'qwertyuiopasdfghjklñzxcvbnmqwertyuiopasdfghjklñzxcvbnmqwerty')

if __name__ == "__main__":
    import __main__
    output = run_test(TCP4_2, data, __main__)