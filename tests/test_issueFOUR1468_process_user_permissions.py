#!/usr/local/bin/python3

'''
These lines will run locally, but will not currently work in the Docker image.
They define the path so that imports from parallel folders can be found.
from sys import path
path.append('../')
'''

import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from test_parent import BaseTest
from util import run_test, login

'''
These are in the format necessary when editing the local path.
from includes.test_parent import BaseTest
from includes.util import run_test, login
'''


class TestUserProcessPermissions(BaseTest):
    ''' Test that users with create/edit process permissions can see the Processes page '''

    def test_user_permissions(self):
        ''' Create User '''

        # Login using configured url, workspace, username, and password
        self.driver = login(data['server_url'], data['username'], data['password'], self.driver)

        # Wait for Requests page to load, verify that inner sidebar is displayed
        wait.until(EC.visibility_of_element_located((By.ID, 'sidebar-inner')))
        self.assertTrue(self.driver.find_element_by_id('sidebar-inner').is_displayed())

        # Click Admin link, wait for +request button to appear to ensure page is loaded 
        self.driver.find_element_by_link_text("Admin").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'navbar-request-button')))
        self.assertTrue(self.driver.find_element_by_id('navbar-request-button').is_displayed())

        # Click the +User button, wait for the modal to appear, populate the fields
        self.driver.find_element_by_xpath("(//button[@type='button'])[5]").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'addUserModal___BV_modal_title_')))
        self.driver.find_element_by_id("username").send_keys("foobar")
        self.driver.find_element_by_id("firstname").send_keys("foo")
        self.driver.find_element_by_id("lastname").send_keys("bar")
        self.driver.find_element_by_id("title").send_keys("foos bars")
        Select(self.driver.find_element_by_name("size")).select_by_visible_text("Active")
        # NOTE: If Selenium fails after user is added, you need to manually edit the username & email address in PM4 to try again
        self.driver.find_element_by_id("email").send_keys("a@a.co")
        self.driver.find_element_by_id("password").send_keys("qqqqqqqq")
        self.driver.find_element_by_id("confpassword").send_keys("qqqqqqqq")
        self.driver.find_element_by_xpath("//footer[@id='addUserModal___BV_modal_footer_']/button[2]").click()

        # Wait for the avatar image button to display
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'avatar-image-button')))
        self.assertTrue(self.driver.find_element_by_class_name('avatar-image-button').is_displayed())

        # Click Permissions link, set Create Processes, ensure Edit Processes also gets checked, save
        # FIXME: Selenium Errors here about "stale element reference: element is not attached to the page document"
        self.driver.find_element_by_id("nav-profile-tab").click()
        self.driver.find_element_by_xpath("//div[@id='accordionPermissions']/div[11]/div/div/button/div[2]/i[2]").click()
        self.driver.find_element_by_id("permission_create-processes").click()
        self.assertTrue(self.driver.find_element_by_id("permission_edit-processes").is_selected())
        self.driver.find_element_by_xpath("(//button[text()='Save'])").click()

        ''' Log in as the new user, go to Designer, verify no errors '''

        self.driver.find_element_by_xpath("//span[@id='avatarMenu']/a/button").click()
        self.driver.find_element_by_link_text("Log Out").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'username')))

        # Log in with new user
        self.driver.find_element_by_id("username").send_keys("foobar")
        self.driver.find_element_by_id("password").send_keys("qqqqqqqq")
        self.driver.find_element_by_id("password").send_keys(Keys.ENTER)
        self.driver.find_element_by_link_text("Designer").click()

        # Wait for Requests page to load, verify that inner sidebar is displayed
        wait.until(EC.visibility_of_element_located((By.ID, 'sidebar-inner')))
        self.assertTrue(self.driver.find_element_by_id('sidebar-inner').is_displayed())

        # Click the Designer link, assert that the Process page loads properly.
        self.driver.find_element_by_link_text("Designer").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'navbar-request-button')))
        self.assertTrue(self.driver.find_element_by_id('navbar-request-button').is_displayed())
        self.assertEqual("Processes - ProcessMaker", self.driver.title)


if __name__ == "__main__":
    import __main__
    output = run_test(TestUserProcessPermissions, data, __main__)
