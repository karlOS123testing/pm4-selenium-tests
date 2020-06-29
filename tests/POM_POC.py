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

from paths.POC import POC as poc_ath
from functions.POC_functions import POM_functions as poc_functions

class POM_POC(poc_functions):
    ''' a string of 60 scharacters can be used in the user search input '''

    def test_POM_POC(self):
        '''Go to the users page and input a 60 characters string in the searchbar'''

        # Login using configured url, workspace, username, and password
        poc_functions.login_POC(self)

        # Go to the admin tab
        poc_functions.go_admin_POC(self)

        # Insert the 60 characters string on the searchbar
        self.driver.find_element_by_class_name("form-control").send_keys('qwertyuiopasdfghjklñzxcvbnmqwertyuiopasdfghjklñzxcvbnmqwerty')
        self.assertEquals(self.driver.find_element_by_class_name("form-control").get_property('value'), 'qwertyuiopasdfghjklñzxcvbnmqwertyuiopasdfghjklñzxcvbnmqwerty')
        
if __name__ == "__main__":
    import __main__
    output = run_test(POM_POC, data, __main__)