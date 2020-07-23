#!/usr/local/bin/python3
""" Collections Page class. """

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class PageCollections:
    ''' Page object model for Collections Page. '''

    def __init__(self, driver, data):
        ''' Instantiate PageCollections class. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 30)

    def paths_collections(self):
        ''' Function to get page elements. '''
        self.new_collection = self.wait.until(EC.visibility_of_element_located((By.ID , 'addUserCollection')))

    def get_page(self):
        ''' Function to navigate to Collections page. '''
        self.driver.get(self.data['server_url'] + '/collections')

    def create_collection(self):
        ''' Click Create Collection button. '''
        self.paths_collections()
        self.new_collection.click()