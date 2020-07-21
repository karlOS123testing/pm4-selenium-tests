# functions for the POM POC

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class PageLogin:
    ''' Page object model for Login Page. '''

    def __init__(self, driver, data):
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 30)

    def paths_login(self):
        self.username_field = self.wait.until(EC.visibility_of_element_located((By.ID, 'username')))
        self.password_field = self.wait.until(EC.visibility_of_element_located((By.ID, 'password')))
        self.login_button = self.wait.until(EC.visibility_of_element_located((By.NAME, 'login')))

    def login(self):
        ''' Function to log user in to workspace.
        '''
        # Navigate to server
        self.driver.get(self.data['server_url'])

        # Login
        self.username_field.send_keys(self.data['username'])
        self.password_field('password').send_keys(self.data['password'])
        self.login_button.click()

        return self.driver
