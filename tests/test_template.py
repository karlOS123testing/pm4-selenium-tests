#!/usr/local/bin/python3
""" Class template to be used for creating new test cases.
"""

# Import methods to get environment
from os import getenv
# Check if tests are run on local machine
# Run tests locally with ENVIRONMENT='local' ./path/to/test.py
if getenv('ENVIRONMENT') == 'local':
    # Import sys.path to add the /includes directory to the path
    # This matches the docker executor's path so local test imports match
    # remote Trogdor test imports
    from sys import path
    path.append('../includes')
    # Import __init__ to include data configuration
    from __init__ import data
# Import BaseTest class where webdriver instance is created
from test_parent import BaseTest
# Import util file where all helper functions are located
import util
# Import all page classes
from page import *
# Import Python unittest module
import unittest


class TestCaseName(BaseTest):
    ''' Brief description of the Test Case. '''

    def setUp(self):
        ''' Method to run before each test method. '''
        # Load server url and note step in log
        self.log.append('Load server url')
        self.driver.get(data['server_url'])

        # Log in and note step in log
        self.log.append('Log in to server')
        login_page = LoginPage(self.driver, data).login()

        # For use with logs
        self.assertionFailures = []

    def tearDown(self):
        ''' Method to run after each test method. '''
        # Runs final assert check. If assertionFailures list is empty, all assertions
        # passed. If it is not empty, assertions failed.
        self.assertEqual([], self.assertionFailures)

    def test_that_login_username_field_accepts_long_strings(self):
        ''' Verify that a string 61+ characters long will be accepted in the username field.'''
        # Perform step tests and note steps in log

        ''' For custom log messages, wrap assertions:

            try:
                # Verify test case
                self.assertTrue(Page.method())

                # Add success message to log if assertion succeeded
                self.log.append('Success message')

            except AssertionError as e:
                # Add failure message to log if assertion failed
                self.log.append('Failure message')

                # Add AssertionError to assertionFailures log
                # This will cause final assertion in tearDown() method to fail
                self.assertionFailures.append(str(e))
        '''

        ''' For simple unittest output:

            # Verify test case
            self.assertTrue(Page.method())
        '''


''' Main call. Only used in test file.
'''
if __name__ == "__main__":

    ''' Import __main__ to use as parameter for method calls.
    '''
    import __main__

    ''' Assign to data as a key, val pair in order to append relative paths and import files.
    repository_path and data are found in the bootstrap.py file for the Docker container.
    Must be referenced in __main__ call and then passed elsewhere. May be edited elsewhere.

    data['repository_path'] = repository_path
    '''

    ''' You may add any key, value pairs to the data object.

    data comes with:
      data['server_url']
      data['username']
      data['password']
    '''

    ''' output is given back to bootstrap.py after the test is run.
    It is a dictionary with "result" and "message" key, value pairs.
    run_test() is the method that provides this dictionary. It requires the class name,
      the data object, and the __main__ module.
    '''
    output = run_test(TestLoginPage, data, __main__)
