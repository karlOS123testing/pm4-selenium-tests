#!/usr/local/bin/python3

# Check if using local environment
from os import getenv

if getenv('ENVIRONMENT') != 'local':
    from test_parent import BaseTest
    from util import run_test
    from includes.file_login import file_login
    
# If using local environment
else:
    from sys import path
    path.append('../')
    from includes.test_parent import BaseTest
    from includes.util import run_test
    from includes.page_login import PageLogin

from __init__ import data
from includes.page_users import PageUsers
from includes.page_menu import PageMenu

class TCP4_1(BaseTest):
    ''' a string of 60 scharacters can be used in the user search input '''

    def test_tcp4_1(self):
        '''Go to the users page and input a 60 characters string in the searchbar'''

        # Login using configured url, workspace, username, and password
        self.driver = PageLogin.login(data['server_url'], data['username'], data['password'], self.driver)

        # Go to the admin tab
        PageMenu.goto_admin(self, self.driver, data)

        # Insert the 60 characters string on the searchbar
        self.assertTrue(PageUsers(self.driver, data).search_long_string())
        
        
if __name__ == "__main__":
    import __main__
    output = run_test(TCP4_1, data, __main__)
    print(output)