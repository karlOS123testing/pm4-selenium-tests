#!/usr/local/bin/python3
# functions for the POM POC

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class PageUserPermissions:
    ''' Page object model for user information page'''

    def __init__(self, driver, data):
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 30)

    def paths_user_permissions(self):
        self.user_information_tab = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='#nav-home']")))       

        try:
            self.english_auth_create_client = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Create Auth Clients')]")))
            self.english_auth_delete_client = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Delete Auth Clients')]")))
            self.english_auth_edit_client = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Edit Auth-Clients')]")))
            self.english_auth_see_client = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'View Auth-Clients')]")))
        except TimeoutException:
            self.english_auth_create_client = 0
            self.english_auth_delete_client = 0
            self.english_auth_edit_client = 0
            self.english_auth_see_client = 0

        self.english_permissions_items = self.english_auth_create_client + self.english_auth_delete_client + self.english_auth_edit_client + self.english_auth_see_client

    def goto_user_permissions(self):
        self.paths_user_permissions()
        self.user_information_tab.click()

    def check_permissions_english_translation(self):
        self.paths_user_permissions()

        if(self.english_permissions_items == 4):
            return True

        else:
            return False