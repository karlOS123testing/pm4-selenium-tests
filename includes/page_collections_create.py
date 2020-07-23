#!/usr/local/bin/python3
""" Create Collections Page class. """

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from page_collections import PageCollections


class PageCreateCollections:
    ''' Page object model for Create Collections Page. '''

    def __init__(self, driver, data):
        ''' Instantiate PageCollections class. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 30)

    def paths_create_collections(self):
        ''' Function to get page elements. '''
        self.name = self.wait.until(EC.visibility_of_element_located((By.ID, 'name')))
        self.description = self.wait.until(EC.visibility_of_element_located((By.ID, 'description')))
        # Double check this xpath
        self.create_screen_dropdown = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[3]//div[1]//div[2]//input[1]")))
        self.view_screen_dropdown = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[4]//div[1]//div[2]//input[1]")))
        self.edit_screen_dropdown = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[5]//div[1]//div[2]//input[1]")))
        self.save_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Save')]")))

    def select_dropdown_menus(self):
        ''' Function to choose screens in dropdown menus. '''
        self.create_screen_dropdown.click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[3]//div[1]//div[3]//ul[1]//li[1]//span[1]"))).click()
        self.view_screen_dropdown.click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[4]//div[1]//div[3]//ul[1]//li[1]//span[1]//span[1]"))).click()
        self.edit_screen_dropdown.click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[5]//div[1]//div[3]//ul[1]//li[1]//span[1]"))).click()

    def get_page(self):
        ''' Function to navigate to Collections page. '''
        PageCollections(self.driver, self.data).create_collection()

    def create_new_collection(self):
        ''' Function create a new collection. '''
        self.get_page()
        self.paths_create_collections()

        self.select_dropdown_menus()
        self.name.send_keys('New Collection')
        self.description.send_keys('New Collection Description')
        self.save_button.click()

    def collection_created(self):
        ''' Function to verify collection is created without error. '''
        self.create_new_collection()

        try:
            self.wait.until(EC.alert_is_present())
            return False
        # Need to run test to find exact exception type
        except:
            return True
