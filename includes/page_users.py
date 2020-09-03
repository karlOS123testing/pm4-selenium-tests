#!/usr/local/bin/python3
""" Users Page class. """

# Check if using local environment
from os import getenv

if getenv('ENVIRONMENT') == 'local':
    # Import sys.path to add the /includes directory to the path
    # This matches the docker executor's path so local test imports match
    # remote Trogdor test imports
    from sys import path
    path.append('../includes')
    # Import __init__ to include data configuration
    from __init__ import data

from page_create_user import PageCreateUser
from page_user_information import PageUserInformation
from page_menu import PageMenu


from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

class PageUsers:
    ''' Page object model for users page'''

    def __init__(self, driver, data):
        ''' Instantiate PageUsers object. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 10)

    def paths_users(self):
        ''' Function to get page elements. '''
        try:
            self.non_admin_user = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//td[text() = '12']/following-sibling::td[@class='vuetable-slot'][2]")))
        # Need to run test to find exact exception type
        except:
            pass
        self.user_search_bar = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='search']")))
        self.create_user_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-secondary']")))

    def search_long_string(self):
        ''' Function to input a long string in the search user bar. '''
        self.paths_users()
        self.user_search_bar.send_keys('qwertyuiopasdfghjklñzxcvbnmqwertyuiopasdfghjklñzxcvbnmqwerty')
        return (self.user_search_bar.get_property('value') == 'qwertyuiopasdfghjklñzxcvbnmqwertyuiopasdfghjklñzxcvbnmqwerty')

    def edit_non_admin(self):
        ''' Function to edit a non admin user. '''
        self.paths_users()
        self.non_admin_user.click()

    def create_user(self):
        ''' Crerates a new user using fill_new_user '''
        self.paths_users()
        self.create_user_button.click()
        PageCreateUser(self.driver, self.data).fill_inactive_user()
        self.create_user_succes = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='alert d-none d-lg-block alertBox alert-dismissible alert-success']")))

    def searchUser(self, findName):
        ''' Search some user'''
        self.searchBox= self.driver.find_element_by_xpath("//*[@id='search']/div/input")
        self.searchBox.send_keys(findName)

        try:
            self.existUsers = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='users-listing']/div[2]/div/div[1]/div/div/h3"))).text          
            print(self.existUsers)
            if self.existUsers == 'No Data Available':
                print("no user found")
                return True
            else:
                print("ok user found")
                return False
        except TimeoutException:
            print("ok user found")
            return False
            
            
        
        
        #self.testvalue = self.driver.find_element_by_xpath("//*[text() = 'testUser']")

        # User check
        #try:    # changes the non-admin user password if it already exists
        #    self.non_admin_user = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//td[text() = '12']/following-sibling::td[@class='vuetable-slot'][2]")))
        #    PageUsers(self.driver, self.data).edit_non_admin()
            #PageUserInformation(self.driver, self.data).change_password()
            #PageMenu(self.driver, self.data).goto_request()
        #    return True

        # Need to run test to find exact exception type
        #except TimeoutException:
        #    PageUsers(self.driver, self.data).create_user()
        #    PageMenu(self.driver, self.data).goto_request()

        #    return False
        

    def create_inactive_user(self, username, password, email, status):
        ''' Create an inactive user'''
        self.paths_users()
        self.create_user_button.click()
        PageCreateUser(self.driver, self.data).fill_inactive_user(username, password, email, status)
        self.create_user_succes = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='alert d-none d-lg-block alertBox alert-dismissible alert-success']")))
