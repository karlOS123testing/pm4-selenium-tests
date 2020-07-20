# functions for the POM POC

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class PageLogin:
    #Paths
    def __init__(self, driver, data):
        self.driver=driver
        self.data=data

    def paths_login(self, driver, data):
        self.username_field = self.driver.find_element_by_id('username')   
        self.password_field = self.driver.find_element_by_id('password')   
       
    @staticmethod     
    def login(url, username, password, driver):
        ''' Function to log user in to workspace.
        '''
        # Navigate to server
        driver.get(url)

        # Wait for login page to load
        wait = WebDriverWait(driver, 30)
        wait.until(EC.element_to_be_clickable((By.NAME, 'login')))

        # Login
        driver.find_element_by_id('username').send_keys(username)
        driver.find_element_by_id('password').send_keys(password)
        driver.find_element_by_name('login').click()

        return driver
