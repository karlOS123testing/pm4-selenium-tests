#!/usr/local/bin/python3
""" New Users Page class. """

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random
import string


class PageCreateUser:
    ''' Page object model for users page'''

    def __init__(self, driver, data):
        ''' Instantiate PageUsers object. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 30)

    def get_random_string(self, length):
        # Random string with the combination of lower and upper case
        letters = string.ascii_letters
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    def paths_create_user(self):
        ''' Function to get page elements. '''
        self.new_user_username = self.wait.until(EC.visibility_of_element_located((By.ID, "username")))
        self.new_user_firstname = self.wait.until(EC.visibility_of_element_located((By.ID, "firstname")))
        self.new_user_lastname = self.wait.until(EC.visibility_of_element_located((By.ID, "lastname")))
        self.new_user_title = self.wait.until(EC.visibility_of_element_located((By.ID, "title")))
        self.new_user_status = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//select[@name='size']")))
        self.new_user_select_status = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//option[contains(text(),'Active')]")))
        self.new_user_email = self.wait.until(EC.visibility_of_element_located((By.ID, "email")))
        self.new_user_password = self.wait.until(EC.visibility_of_element_located((By.ID, "password")))
        self.new_user_confpassword = self.wait.until(EC.visibility_of_element_located((By.ID, "confpassword")))

        self.char_set = string.ascii_letters
        self.user_pass = self.get_random_string(8)

        self.new_user_save = self.wait.until(EC.visibility_of_element_located((By.ID, "saveUser")))

    def fill_new_user(self):
        self.paths_create_user()
        self.new_user_username.send_keys(self.get_random_string(8))
        self.new_user_firstname.send_keys(self.get_random_string(8))
        self.new_user_lastname.send_keys(self.get_random_string(8))
        self.new_user_title.send_keys(self.get_random_string(8))
        self.new_user_status.click()
        self.new_user_select_status.click()
        self.new_user_email.send_keys(self.get_random_string(8)+"@processmaker.com")
        self.new_user_password.send_keys(self.user_pass)
        self.new_user_confpassword.send_keys(self.user_pass)
        self.new_user_save.click()
