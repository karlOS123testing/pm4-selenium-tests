#!/usr/local/bin/python3
""" User Permissions Page class. """

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class PageUserPermissions:
    ''' Page object model for user permissions page'''

    def __init__(self, driver, data):
        ''' Instantiate PageUserInformation object. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 30)

    def paths_user_permissions(self):
        ''' Function to get page elements. '''
        self.user_information_tab = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='#nav-home']")))              
        self.auth_accordeon = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@data-target= '#auth-clients']")))     

        # Looks for the translated strings on permissions
        try:
            self.english_auth_create_client = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Create Auth Clients')]")))
            self.english_auth_delete_client = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Delete Auth Clients')]")))
            self.english_auth_edit_client = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Edit Auth-Clients')]")))
            self.english_auth_see_client = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'View Auth-Clients')]")))

            self.bool_english_permissions_items = True
        except TimeoutException:
            self.bool_english_permissions_items = False

    def goto_user_permissions(self):
        self.paths_user_permissions()
        self.user_information_tab.click()

    def open_auth_accordeon(self):
        self.paths_user_permissions()
        self.auth_accordeon.click()

    def check_permissions_english_translation(self):
        self.paths_user_permissions()

        if self.bool_english_permissions_items:
            return True

        else:
            return False