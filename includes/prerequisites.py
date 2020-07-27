#!/usr/local/bin/python3
""" Prerequisites set """

from includes.page_users import PageUsers
from includes.page_create_user import PageCreateUser
from includes.page_menu import PageMenu
from includes.page_user_information import PageUserInformation
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Prerequisites:
    ''' Functions used to check for prerequisites'''

    def __init__(self, driver, data):
        ''' Instantiate PageUsers object. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 30)

    def check_users_exists(self):
        ''' Check if there are 2 users, create one if not'''

        # User check
        try:    # changes the non-admin user password if it already exists
            self.non_admin_user = self.wait.until(EC.visibility_of_element_located((By.XPATH, "(//button[@title='Edit'])[2]")))
            PageUsers(self.driver, self.data).edit_non_admin()
            PageUserInformation(self.driver, self.data).change_password()
            PageMenu(self.driver, self.data).goto_admin()
            return True

        # Need to run test to find exact exception type
        except TimeoutException:
            PageUsers(self.driver, self.data).create_user()
            PageMenu(self.driver, self.data).goto_admin()
            return False
