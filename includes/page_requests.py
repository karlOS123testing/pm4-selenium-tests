#!/usr/local/bin/python3
""" Requests Page class. """

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class PageRequests:
    ''' Page object model for Auth Clients Page. '''

    def __init__(self, driver, data):
        ''' Instantiate PageRequests class. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 30)

    def paths_requests(self):
        ''' Function to get page elements. '''
        self.navigation_bar = self.wait.until(EC.visibility_of_element_located((By.ID, 'nav_collapse')))

    def get_page(self):
        ''' Function to navigate to Requests page. '''
        self.driver.get(self.data['server_url'] + '/requests')

    def timeout_alert_present(self):
        ''' Function to check if the Timeout alert appears when navigating to Requests page. '''
        self.get_page()
        try:
            self.wait.until(EC.alert_is_present())
            'Timeout' in self.driver.page_source()
            return True
        # Need to run test to find exact exception type
        except:
            return False
