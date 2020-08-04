#!/usr/local/bin/python3

from selenium.webdriver.support.ui import WebDriverWait

class BasePageElement(object):
    """ Base Page Element class that's initialized on every Page Object class. """

    def __set__(self, obj, value):
        ''' Set the text to the value supplied. '''
        driver = obj.driver
        WebDriverWait(driver, 30).until(
            lambda driver: driver.find_element_by_id(self.locator)
        )
        driver.find_element_by_id(self.locator).clear()
        driver.find_element_by_id(self.locator).send_keys(value)

    def __get__(self, obj, owner):
        ''' Get the text of specified object. '''
        driver = obj.driver
        WebDriverWait(driver, 30).until(
            lambda driver: driver.find_element_by_id(self.locator)
        )
        element = driver.find_element_by_id(self.locator)
        return element.get_attribute("value")
