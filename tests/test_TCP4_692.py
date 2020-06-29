#!/usr/local/bin/python3

# Check if using local environment
from os import getenv

if getenv('ENVIRONMENT') != 'local':
    from test_parent import BaseTest
    from util import run_test, login
# If using local environment
else:
    from sys import path
    path.append('../')
    from includes.test_parent import BaseTest
    from includes.util import run_test, login

import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TCP4_692(BaseTest):
    ''' Test that a token can be added to the user'''

    def test_tcp4_692(self):
        '''Adds a token to the user'''

        # Login using configured url, workspace, username, and password
        self.driver = login(data['server_url'], data['username'], data['password'], self.driver)

        # Redirect to Admin Users page, wait for +User button to be clickable 
        self.driver.get(data['server_url'] + '/admin/users')
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'vuetable-body')))
        
        # Find table record with ID = '2', find edit button in this element, and click
        user_tr = self.driver.find_element_by_xpath("//tr//td[1][contains(text(), '2')]").find_element_by_xpath("..")
        user_tr.find_element_by_class_name('fa-pen-square').click()
             
        # Go to the tokens tab
        self.wait.until(EC.visibility_of_element_located((By.ID, 'nav-tokens-tab')))
        self.driver.find_element_by_id('nav-tokens-tab').click()

        # Get the number of tokens
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[id='nav-tokens']>div>div>button")))
        elements_before =self.driver.find_elements_by_css_selector("td[class='vuetable-slot']")
        before_size = len(elements_before)

        # Create a new token
        self.driver.find_element_by_css_selector("div[id='nav-tokens']>div>div>button").click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='modal-content p-3']")))
        self.driver.find_element_by_css_selector("button[class='ml-auto btn btn-outline-secondary']").click()

        # Confirm the token was created       
        self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "div[class='modal-content p-3']")))
        self.wait.until(EC.visibility_of_element_located((By.ID, 'nav-tokens-tab')))
        elements_after =self.driver.find_elements_by_css_selector("td[class='vuetable-slot']")    
        after_size = len(elements_after)
        self.wait.until(EC.visibility_of_element_located((By.ID, 'nav-tokens')))
        self.assertEqual(after_size, before_size+1)

if __name__ == "__main__":
    import __main__    
    output = run_test(TCP4_692, data, __main__)