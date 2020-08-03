#!/usr/local/bin/python3
""" Module to contain helper functions that cut down on redundant code in main calls.
"""

import unittest
from contextlib import redirect_stdout
from io import StringIO
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from test_classes import CustomTextTestRunner, CustomTestLoader


def run_test(classname, data, modulename):
    ''' Function to run test and redirect output from stdout
        and return results in PM4 output variable.
    '''
    if data is {}:
        return 'data dictionary must not be empty'

    if not classname:
        return 'classname missing'

    if not data:
        return 'data missing'

    if not modulename:
        return 'modulename missing'

    suite = CustomTestLoader().loadTestsFromModule(modulename)
    classname.data = data
    with StringIO() as buffer:
        with redirect_stdout(buffer):
            log = CustomTextTestRunner(stream=buffer).run(suite).log
            if 'ERROR' in log[-1]:
                log[-1] = parse_log_error(log[-1])
            elif 'WARNING' in log[-1]:
                log[-1] = parse_log_warning(log[-1])
            test_output = buffer.getvalue()
            return {"result": parse_results(test_output), "message": test_output}

def parse_results(buffer):
    ''' Function to parse the unittest results into PM4-friendly format.
    '''
    if not buffer or buffer is '':
        return 'No unittest result detected'

    if buffer.startswith('.'):
        return 'SUCCESS'
    elif buffer.startswith('F'):
        return 'FAIL'
    else:
        return 'ERROR'

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
