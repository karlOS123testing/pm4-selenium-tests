#!/usr/local/bin/python3
" local test, dont push to git "

# Check if using local environment
from os import getenv

if getenv('ENVIRONMENT') != 'local':
    from test_parent import BaseTest
    from util import run_test
    from page_login import PageLogin
    from page_users import PageUsers
    from page_user_information import PageUserInformation
    from page_menu import PageMenu
    from prerequisites import Prerequisites
    from page_user_permissions import PageUserPermissions

    
# If using local environment
else:
    from sys import path
    path.append('../')
    from includes.test_parent import BaseTest
    from includes.util import run_test
    from includes.page_login import PageLogin
    from includes.page_users import PageUsers
    from includes.page_user_information import PageUserInformation
    from includes.page_menu import PageMenu
    from includes.prerequisites import Prerequisites
    from includes.page_user_permissions import PageUserPermissions
    from __init__ import data


class Four283(BaseTest):
    ''' a string of 60 scharacters can be used in the user search input '''

    def test_four_283(self):
        '''Go to the users page and input a 60 characters string in the searchbar'''

        # Login using configured url, workspace, username, and password
        self.driver = PageLogin(self.driver, data).login()

        # Go to the admin tab
        PageMenu(self.driver, data).goto_admin()

        # Test for prerequisites
        Prerequisites(self.driver, data).check_users_exists() 

        # Go to user information and change the language
        PageUsers(self.driver, data).edit_non_admin()
        PageUserInformation(self.driver, data).change_user_language("english")
        PageUserInformation(self.driver, data).goto_user_permissions()

        # Opens the auth permissions and check for translation     
        PageUserPermissions(self.driver, data).open_auth_accordeon()
        self.assertTrue(PageUserPermissions(self.driver, data).check_permissions_english_translation())

        
        
if __name__ == "__main__":
    import __main__
    output = run_test(Four283, data, __main__)
    print(output)