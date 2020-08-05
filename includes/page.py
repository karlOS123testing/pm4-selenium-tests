#!/usr/local/bin/python3

from element import *
from locators import *
import util

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
    Classes:
        BasePageShell:
            Initializes driver, data, and page_url attributes.
            Includes go_to_page and is_url_matches methods.
            These attributes and methods are available to all BasePage classes
                and classes that inherit from BasePage and BasePageShell classes.

        BasePage:
            Includes click_requests_link, click_tasks_link,
                click_designer_link, click_admin_link, and click_avatar methods.
            These methods are available to all Page classes that inherit from
                BasePage classes.
"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class BasePageShell(object):
    """ Base page shell class from which two classes inherit:
            BasePage
            LoginPage
    """

    def __init__(self, driver, data):
        ''' Initializes each page with three attributes:
                driver:
                    instantited in /includes/test_parent.py.
                data:
                    provided through config task on Trogdor server
                    or through data defined in local __init__ file.
                page_url:
                    provided in data.
        '''
        self.driver = driver
        self.data = data
        self.page_url = self.data['server_url']

    def go_to_page(self):
        ''' Navigates to page_url:
                provided through config task on Trogdor server
                or through data defined in local __init__ file.
        '''
        self.driver.get(self.page_url)


class BasePage(BasePageShell):
    """ Base page class from which other page classes inherit.

        These methods are made available to all Page classes, aside from LoginPage,
            because these navigation links are all available on each page.

        BasePageLocators are found in /includes/locators.py.
    """

    def click_requests_link(self):
        ''' Locates and clicks on Requests link in navigation bar. '''
        element = self.driver.find_element(*BasePageLocators.REQUESTS_LINK)
        element.click()

    def click_tasks_link(self):
        ''' Locates and clicks on Tasks link in navigation bar. '''
        element = self.driver.find_element(*BasePageLocators.TASKS_LINK)
        element.click()

    def click_designer_link(self):
        ''' Locates and clicks on Designer link in navigation bar. '''
        element = self.driver.find_element(*BasePageLocators.DESIGNER_LINK)
        element.click()

    def click_admin_link(self):
        ''' Locates and clicks on Admin link in navigation bar. '''
        element = self.driver.find_element(*BasePageLocators.ADMIN_LINK)
        element.click()

    def click_avatar(self):
        ''' Locates and clicks on Avatar icon in navigation bar. '''
        element = self.driver.find_element(*BasePageLocators.AVATAR)
        element.click()


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
    Login Page: /login
    Classes:
        LoginPage
        UsernameFieldElement
        PasswordFieldElement
"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class UsernameFieldElement(BasePageElement):
    """ Class to get search text from specified locator. """

    # Locator for search box where string is entered
    locator = 'username'


class PasswordFieldElement(BasePageElement):
    """ Class to get search text from specified locator. """

    # Locator for search box where string is entered
    locator = 'password'


class LoginPage(BasePageShell):
    """ Login Page actions. """

    def __init__(self, driver, data):
        ''' Instantiate LoginPage class. '''
        super(LoginPage, self).__init__(driver, data)
        self.page_url = self.page_url + '/login'

    username_field_element = UsernameFieldElement('ID')
    password_field_element = PasswordFieldElement('ID')

    def login(self):
        ''' Function to log user in to workspace.
        '''
        # Login
        self.username_field_element = self.data['username']
        self.password_field_element = self.data['password']
        login_button_element = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button_element.click()

        return self.driver


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
    Requests Page: /requests
    Classes:
        RequestsPage
"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class RequestsPage(BasePage):
    """ Requests Page actions. """

    def __init__(self, driver, data):
        ''' Instantiate RequestsPage class. '''
        super(DesignerPage, self).__init__(driver, data)
        self.page_url = self.page_url + '/requests'

    def click_my_requests_button(self):
        ''' Clicks on My Requests. '''
        element = self.driver.find_element(*RequestsPageLocators.MY_REQUESTS)
        element.click()

    def click_in_progress_button(self):
        ''' Clicks on In Progress. '''
        element = self.driver.find_element(*RequestsPageLocators.IN_PROGRESS)
        element.click()

    def click_completed_button(self):
        ''' Clicks on Completed. '''
        element = self.driver.find_element(*RequestsPageLocators.COMPLETED)
        element.click()

    def click_all_requests_button(self):
        ''' Clicks on All Requests. '''
        element = self.driver.find_element(*RequestsPageLocators.ALL_REQUESTS)
        element.click()


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
    Admin Page: /admin/users
    Classes:
        AdminPage
"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class AdminPage(BasePage):
    """ Admin Page actions. """

    def __init__(self, driver, data):
        ''' Instantiate DesignerPage class. '''
        super(AdminPage, self).__init__(driver, data)
        self.page_url = self.page_url + '/admin/users'

    def click_users_tab(self):
        ''' Clicks on Users tab. '''
        element = self.driver.find_element(*AdminPageLocators.USERS_TAB)
        element.click()

    def click_deleted_users_tab(self):
        ''' Clicks on Users tab. '''
        element = self.driver.find_element(*AdminPageLocators.DELETED_USERS_TAB)
        element.click()

    def click_users_button(self):
        ''' Clicks on Users tab. '''
        element = self.driver.find_element(*AdminPageLocators.USERS_BUTTON)
        element.click()

    def click_groups_button(self):
        ''' Clicks on Users tab. '''
        element = self.driver.find_element(*AdminPageLocators.GROUPS_BUTTON)
        element.click()

    def click_auth_clients_button(self):
        ''' Clicks on Users tab. '''
        element = self.driver.find_element(*AdminPageLocators.AUTH_CLIENTS_BUTTON)
        element.click()

    def click_customize_ui_button(self):
        ''' Clicks on Users tab. '''
        element = self.driver.find_element(*AdminPageLocators.CUSTOMIZE_UI_BUTTON)
        element.click()

    def click_queue_management_button(self):
        ''' Clicks on Users tab. '''
        element = self.driver.find_element(*AdminPageLocators.QUEUE_MANAGEMENT_BUTTON)
        element.click()

    def click_script_executors_button(self):
        ''' Clicks on Users tab. '''
        element = self.driver.find_element(*AdminPageLocators.SCRIPT_EXECUTORS_BUTTON)
        element.click()


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
    Designer Page: /processes
    Classes:
        DesignerPage
"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class DesignerPage(BasePage):
    """ Designer Page actions. """

    def __init__(self, driver, data):
        ''' Instantiate DesignerPage class. '''
        super(AdminPage, self).__init__(driver, data)
        self.page_url = self.data['server_url'] + '/processes'

    def click_processes_tab(self):
        ''' Clicks on Processes tab. '''
        element = self.driver.find_element(*DesignerPageLocators.PROCESSES_TAB)
        element.click()

    def click_categories_tab(self):
        ''' Clicks on Processes tab. '''
        element = self.driver.find_element(*DesignerPageLocators.CATEGORIES_TAB)
        element.click()

    def click_archived_processes_tab(self):
        ''' Clicks on Processes tab. '''
        element = self.driver.find_element(*DesignerPageLocators.ARCHIVED_PROCESSES_TAB)
        element.click()

    def click_processes_button(self):
        ''' Clicks on Processes tab. '''
        element = self.driver.find_element(*DesignerPageLocators.PROCESSES_BUTTON)
        element.click()

    def click_scripts_button(self):
        ''' Clicks on Processes tab. '''
        element = self.driver.find_element(*DesignerPageLocators.SCRIPTS_BUTTON)
        element.click()

    def click_screens_button(self):
        ''' Clicks on Processes tab. '''
        element = self.driver.find_element(*DesignerPageLocators.SCREENS_BUTTON)
        element.click()

    def click_environment_variables_button(self):
        ''' Clicks on Processes tab. '''
        element = self.driver.find_element(*DesignerPageLocators.ENVIRONMENT_VARIABLES_BUTTON)
        element.click()
