#!/usr/local/bin/python3
""" Page Navigation class. """

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


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
