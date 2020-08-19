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
        self.driver.get(self.data['server_url'] + '/admin/users')

    def goto_request(self):
        ''' Function to navigate to the request tab. '''
        self.driver.get(self.data['server_url'] + '/admin/request')

    def log_out(self):
        ''' Logs out the current user '''
        self.wait.until(EC.visibility_of_element_located((By.ID, 'avatarMenu')))
        self.driver.find_element_by_id("avatarMenu").click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "li>a[href='/logout']")))
        self.driver.find_element_by_css_selector("li>a[href='/logout']").click()
        