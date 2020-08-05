#!/usr/local/bin/python3
""" Module to contain helper functions that cut down on redundant code in main calls.
"""

import random
import string
from contextlib import redirect_stdout
from io import StringIO
from test_classes import CustomTextTestRunner, CustomTestLoader


def run_test(classname, data, modulename):
    ''' Function to run test and redirect output from stdout
        and return results in PM4 output variable.
    '''
    if data is {}:
        return {"result": "FAIL", "message": "Cannot run test. data configuration empty."}

    if not classname:
        return {"result": "FAIL", "message": "Cannot run test. classname missing."}

    if not data:
        return {"result": "FAIL", "message": "Cannot run test. data missing."}

    if not modulename:
        return {"result": "FAIL", "message": "Cannot run test. modulename missing."}

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
    elif buffer.startswith('F') or buffer.startswith('E'):
        return 'FAIL'

def generate_long_text():
    ''' Function to generate a random string 95 chars long. '''
    return ''.join(random.choice(string.ascii_letters) for n in range(95))

def generate_text():
    ''' Function to generate a random string 10 chars long. '''
    return ''.join(random.choice(string.ascii_letters) for n in range(10))

def generate_email():
    ''' Function to generate a random email. '''
    return ''.join(random.choice(string.ascii_letters) for n in range(10)) +\
        '@' + ''.join(random.choice(string.ascii_letters) for n in range(5)) +\
        '.' + ''.join(random.choice(string.ascii_letters) for n in range(5))
