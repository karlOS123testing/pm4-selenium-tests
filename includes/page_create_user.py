#!/usr/local/bin/python3
""" New Users Page class. """

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class PageCreateUser:
    ''' Page object model for users page'''

    def __init__(self, driver, data):
        ''' Instantiate PageUsers object. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 30)

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

        self.new_user_save = self.wait.until(EC.visibility_of_element_located((By.ID, "saveUser")))

    def fill_new_user(self):
        self.paths_create_user()
        self.new_user_username.send_keys('Bot')
        self.new_user_firstname.send_keys('trogdor')
        self.new_user_lastname.send_keys('selenium')
        self.new_user_title.send_keys('Automation')
        self.new_user_status.click()
        self.new_user_select_status.click()
        self.new_user_email.send_keys('trogdor@processmaker.comn')
        self.new_user_password.send_keys('Trogdor123')
        self.new_user_confpassword.send_keys('Trogdor123')
        self.new_user_save.click()
