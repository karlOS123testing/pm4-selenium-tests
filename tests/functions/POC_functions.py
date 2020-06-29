# functions for the POM POC
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
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class POM_functions(BaseTest):
    ''' a string of 60 scharacters can be used in the user search input '''

    def login_POC(self):
        '''Go to the users page and input a 60 characters string in the searchbar'''

        # Login using configured url, workspace, username, and password
        self.driver = login(data['server_url'], data['username'], data['password'], self.driver)

    def go_admin_POC(self):
        '''Go to the users page and input a 60 characters string in the searchbar'''
        # Go to the admin tab
        self.driver.get(data['server_url'] + '/admin/users')
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "form-control")))

if __name__ == "__main__":
    import __main__
    output = run_test(POM_functions, data, __main__)