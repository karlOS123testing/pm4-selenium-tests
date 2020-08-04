#!/usr/local/bin/python3

from selenium.webdriver.support.ui import WebDriverWait

""" BasePageElement classes.
    Descriptors for getting and setting single elements.
        ID
        NAME
        XPATH
"""

class BasePageElement(object):
    """ Base Page Element class that's initialized on every Page Object class. """
    def __init__(self, element_type=None):
        ''' Initialize the BasePageElement object with its correct locator type. '''
        self.element_type = element_type

    def __set__(self, obj, value):
        ''' Set the text to the value supplied. '''
        driver = obj.driver
        if self.element_type == 'ID':
            WebDriverWait(driver, 30).until(
                lambda driver: driver.find_element_by_id(self.locator)
            )
            driver.find_element_by_id(self.locator).clear()
            driver.find_element_by_id(self.locator).send_keys(value)
        elif self.element_type == 'NAME':
            WebDriverWait(driver, 30).until(
                lambda driver: driver.find_element_by_name(self.locator)
            )
            driver.find_element_by_name(self.locator).clear()
            driver.find_element_by_name(self.locator).send_keys(value)
        elif self.element_type == 'XPATH':
            WebDriverWait(driver, 30).until(
                lambda driver: driver.find_element_by_xpath(self.locator)
            )
            driver.find_element_by_xpath(self.locator).clear()
            driver.find_element_by_xpath(self.locator).send_keys(value)

    def __get__(self, obj, owner):
        ''' Get the text of specified object. '''
        driver = obj.driver
        if self.element_type == 'ID':
            WebDriverWait(driver, 30).until(
                lambda driver: driver.find_element_by_id(self.locator)
            )
            element = driver.find_element_by_id(self.locator)
        elif self.element_type == 'NAME':
            WebDriverWait(driver, 30).until(
                lambda driver: driver.find_element_by_name(self.locator)
            )
            element = driver.find_element_by_name(self.locator)
        elif self.element_type == 'XPATH':
            WebDriverWait(driver, 30).until(
                lambda driver: driver.find_element_by_xpath(self.locator)
            )
            element = driver.find_element_by_xpath(self.locator)
        return element.get_attribute("value")
