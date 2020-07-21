#!/usr/local/bin/python3
# functions for the POM POC

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Check if using local environment
from os import getenv

#if getenv('ENVIRONMENT') != 'local':
 #   from test_parent import BaseTest
  #  from util import run_test
   # from page_login import PageLogin
    #from page_users import PageUsers
    #from page_menu import PageMenu

    
# If using local environment
#else:
from sys import path
path.append('../')
from includes.test_parent import BaseTest
from includes.util import run_test
from includes.page_login import PageLogin
from __init__ import data
from includes.page_users import PageUsers


class PageMenu:
    ''' Page object model for Navigation Menu. '''

    def __init__(self, driver, data):
        ''' Instantiate PageMenu object. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(self.driver, 30)

    def goto_admin(self):
        ''' Function to navigate to the admin tab. '''
        self.driver.get(data['server_url'] + '/admin/users')
