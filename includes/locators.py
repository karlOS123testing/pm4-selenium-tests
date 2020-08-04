#!/usr/local/bin/python3

from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    """ Class for Login Page locators. All Login page locators here. """
    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.NAME, 'login')

class DesignerPageLocators(object):
    """ Class for Designer Page locators. All Designer page locators here. """
    MY_REQUESTS = (By.XPATH, "//i[@class='fas nav-icon fa-id-badge']")
    IN_PROGRESS = (By.XPATH , "//i[@class='fas nav-icon fa-clipboard-list']")
    COMPLETED = (By.XPATH , "//i[@class='fas nav-icon fa-clipboard-check']")
    ALL_REQUESTS = (By.XPATH , "//i[@class='fas nav-icon fa-clipboard']")
