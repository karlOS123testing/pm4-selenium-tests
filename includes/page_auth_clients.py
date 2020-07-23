#!/usr/local/bin/python3
""" Auth Clients Page class. """

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class PageAuthClients:
    ''' Page object model for Auth Clients Page. '''

    def __init__(self, driver, data):
        ''' Instantiate PageAuthClients class. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 30)

    def paths_auth_clients(self):
        ''' Function to get page elements. '''

    def get_page(self):
        ''' Function to navigate to Auth Clients page. '''
        self.driver.get(self.data['server_url'] + '/admin/auth-clients')
