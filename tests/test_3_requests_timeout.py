#!/usr/local/bin/python3

# Check if using local environment
from os import getenv

if getenv('ENVIRONMENT') == 'local':
    from sys import path
    path.append('../')
    from includes.test_parent import BaseTest
    from includes.util import run_test
    from includes.page_login import PageLogin
    from __init__ import data
    from includes.page_users import PageUsers
    from includes.page_menu import PageMenu
    from includes.page_requests import PageRequests

    
# If using local environment
else:
    from test_parent import BaseTest
    from util import run_test
    from page_login import PageLogin
    from page_users import PageUsers
    from page_menu import PageMenu
    from page_requests import PageRequests


class TestRequestsTimeout(BaseTest):
    ''' Class to check Requests timeout. '''

    def test_requests_page_no_timeout(self):
        ''' Test that Requests page doesn't give a timeout alert upon loading. '''
        # Log in
        self.driver = PageLogin(self.driver, data).login()

        # Check Requests page doesn't give a timeout error
        self.assertFalse(PageRequests(self.driver, data).timeout_alert_present())


if __name__ == "__main__":
    import __main__
    output = run_test(TestRequestsTimeout, data, __main__)
