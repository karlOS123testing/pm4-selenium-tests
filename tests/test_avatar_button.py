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
    from __init__ import data

import unittest
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TestAvatarImageButton(BaseTest):
    ''' Navigate to Admin page and create a new user. '''

    def test_avatar_image_button(self):
        ''' Test that avatar image button displays after new user creation. '''

        # Login using configured url, workspace, username, and password
        self.driver = login(data['server_url'], data['username'], data['password'], self.driver)

        # Wait for Requests page to load until inner sidebar is displayed
        self.wait.until(EC.visibility_of_element_located((By.ID, 'sidebar-inner')))

        # Click Admin link, wait for +request button to appear to ensure page is loaded 
        self.driver.find_element_by_link_text("Admin").click()
        self.wait.until(EC.visibility_of_element_located((By.ID, 'navbar-request-button')))

        # Click the +User button, wait for the modal to appear, populate the fields
        self.driver.find_element_by_xpath("(//button[@type='button'])[5]").click()
        self.wait.until(EC.visibility_of_element_located((By.ID, 'addUserModal___BV_modal_title_')))
        self.driver.find_element_by_id("username").send_keys("newuser")
        self.driver.find_element_by_id("firstname").send_keys("foo")
        self.driver.find_element_by_id("lastname").send_keys("bar")
        self.driver.find_element_by_id("title").send_keys("foos bars")
        Select(self.driver.find_element_by_name("size")).select_by_visible_text("Active")
        
        # NOTE: If Selenium fails after user is added, you need to manually edit the username & email address in PM4 to try again
        # Or edit the code and create new username and email address
        self.driver.find_element_by_id("email").send_keys("anew@a.co")
        self.driver.find_element_by_id("password").send_keys("qqqqqqqq")
        self.driver.find_element_by_id("confpassword").send_keys("qqqqqqqq")
        self.driver.find_element_by_xpath("//footer[@id='addUserModal___BV_modal_footer_']/button[2]").click()

        # Wait for the avatar image button to display
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'avatar-image-button')))
        self.assertTrue(self.driver.find_element_by_class_name('avatar-image-button').is_displayed())


if __name__ == "__main__":
    import __main__
    output = run_test(TestAvatarImageButton, data, __main__)
