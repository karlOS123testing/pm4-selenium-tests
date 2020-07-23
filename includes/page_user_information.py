#!/usr/local/bin/python3
""" User Info Page class. """

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class PageUserInformation:
    ''' Page object model for user information page'''

    def __init__(self, driver, data):
        ''' Instantiate PageUserInformation object. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 30)

    def paths_user_information(self):
        ''' Function to get page elements. '''
        self.user_permissions_tab = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='#nav-profile']")))

        self.user_language = self.wait.until(EC.visibility_of_element_located((By.ID, "language")))
        # self.user_language_deutch = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//option[@value='de']")))
        self.user_language_english = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//option[@value='en']")))
        # self.user_language_spanish = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//option[@value='es']")))
        # self.user_language_french = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//option[@value='fr']")))

    def goto_user_permissions(self):
        ''' Click on the user permissions tab'''
        self.paths_user_information()
        self.user_permissions_tab.click()

    def change_user_language(self, selected_language):
        ''' Changes the language for the user to the specified one'''
        self.paths_user_information()
        self.user_language.click()
        self.switch_language(selected_language)

    def switch_language(self, selected_language):
        ''' Switch to click on the language selected'''
        switcher = {
            # "deutch": self.user_language_deutch.click(),
            "english": self.user_language_english.click(),
            # "spanish": self.user_language_spanish.click(),
            # "french": self.user_language_french.click()
        }
