#!/usr/local/bin/python3
# functions for the POM POC

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class PageUserInformation:
    ''' Page object model for user information page'''

    def __init__(self, driver, data):
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 30)

    def paths_user_information(self):
        self.user_permissions_tab = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='#nav-profile']")))   

    def goto_user_permissions(self):
        self.paths_user_information()
        self.user_permissions_tab.click()
