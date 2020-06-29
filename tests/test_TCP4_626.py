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

class TCP4_626(BaseTest):
    ''' Test that the user process designer group can be changed '''

    def test_tcp4_626(self):
        '''Edits the user process dessigner group status'''

        # Login using configured url, workspace, username, and password
        self.driver = login(data['server_url'], data['username'], data['password'], self.driver)

        # Redirect to Admin Users page, wait for +User button to be clickable 
        self.driver.get(data['server_url'] + '/admin/users')
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'vuetable-body')))
        
        # Find table record with ID = '2', find edit button in this element, and click
        user_tr = self.driver.find_element_by_xpath("//tr//td[1][contains(text(), '2')]").find_element_by_xpath("..")
        user_tr.find_element_by_class_name('fa-pen-square').click()
        
        # Go to the groups tab
        self.wait.until(EC.visibility_of_element_located((By.ID, 'nav-groups-tab')))
        self.driver.find_element_by_id('nav-groups-tab').click()

        # If View Groups toggle is already selected, turn on 'unselected' bool
        self.wait.until(EC.visibility_of_element_located((By.ID, "nav-groups")))
        if self.driver.find_element_by_css_selector("div>input[id='switch_2']").is_selected():
            unselected = True
        else:
            unselected = False

        # Interact with the process designers group slider, save and wait for success alert
        # Uses JSexecutor as a normal click wont work
        javaScript = "document.getElementById('switch_2').click();"
        self.driver.execute_script(javaScript)
        self.driver.find_element_by_id('saveGroups').click()
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "alert-success")))

        # Redirect to Admin Users page, wait for +User button to be clickable 
        self.driver.get(data['server_url'] + '/admin/users')
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'vuetable-body')))

        # Find table record with ID = '2', find edit button in this element, and click
        user_tr = self.driver.find_element_by_xpath("//tr//td[1][contains(text(), '2')]").find_element_by_xpath("..")
        user_tr.find_element_by_class_name('fa-pen-square').click()
        
        # Go to the groups tab
        self.wait.until(EC.visibility_of_element_located((By.ID, 'nav-groups-tab')))
        self.driver.find_element_by_id('nav-groups-tab').click()

        # Verify process designer Group togglehas changed
        self.wait.until(EC.visibility_of_element_located((By.ID, "nav-groups")))
        if unselected:
            self.assertFalse(self.driver.find_element_by_css_selector("div>input[id='switch_2']").is_selected())
        else:
            self.assertTrue(self.driver.find_element_by_css_selector("div>input[id='switch_2']").is_selected())

if __name__ == "__main__":
    import __main__  
    output = run_test(TCP4_626, data, __main__)