from element import *
from locators import *
import util


class UsernameFieldElement(BasePageElement):
    """ Class to get search text from specified locator. """

    # Locator for search box where string is entered
    locator = 'username'

class BasePage(object):
    """ Base page class from which other page classes inherit. """

    def __init__(self, driver, data):
        self.driver = driver
        self.data = data


class LoginPage(BasePage):
    """ Login Page actions. """

    def __init__(self, driver, data):
        ''' Instantiate LoginPage class. '''
        super(LoginPage, self).__init__(driver, data)
        self.page_url = self.data['server_url'] + '/login'

    username_field_element = UsernameFieldElement('ID')

    def is_url_matches(self):
        ''' Verifies page URL matches login page. '''
        return self.driver.current_url == self.page_url

    def login(self):
        ''' Function to log user in to workspace.
        '''
        # Login
        self.driver.find_element_by_id('username').send_keys(self.data['username'])
        self.driver.find_element_by_id('password').send_keys(self.data['password'])
        self.driver.find_element_by_name('login').click()

        return self.driver


class DesignerPage(BasePage):
    """ Designer Page actions. """

    def __init__(self, driver, data):
        ''' Instantiate DesignerPage class. '''
        super(DesignerPage, self).__init__(driver, data)
        self.page_url = self.data['server_url'] + '/processes'

    def go_to_page(self):
        ''' Navigates to page. '''
        self.driver.get(self.page_url)

    def is_url_matches(self):
        ''' Verifies page URL matches processes route. '''
        return self.driver.current_url == self.page_url

    def click_my_requests_button(self):
        ''' Clicks on My Requests. '''
        element = self.driver.find_element(*DesignerPageLocators.MY_REQUESTS)
        element.click()

    def click_in_progress_button(self):
        ''' Clicks on In Progress. '''
        element = self.driver.find_element(*DesignerPageLocators.IN_PROGRESS)
        element.click()

    def click_completed_button(self):
        ''' Clicks on Completed. '''
        element = self.driver.find_element(*DesignerPageLocators.COMPLETED)
        element.click()

    def click_all_requests_button(self):
        ''' Clicks on All Requests. '''
        element = self.driver.find_element(*DesignerPageLocators.ALL_REQUESTS)
        element.click()

class AdminPage(BasePage):
    """ Admin Page actions. """

    def __init__(self, driver, data):
        ''' Instantiate DesignerPage class. '''
        super(AdminPage, self).__init__(driver, data)
        self.page_url = self.data['server_url'] + '/admin/users'

    def go_to_page(self):
        ''' Navigates to page. '''
        self.driver.get(self.page_url)

    def is_url_matches(self):
        ''' Verifies page URL matches processes route. '''
        return self.driver.current_url == self.page_url

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
