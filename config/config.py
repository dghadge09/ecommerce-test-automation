"""
Configuration file for E-Commerce Test Automation Framework
"""


class Config:
    # Application URL
    BASE_URL = 'https://www.saucedemo.com/'

    # Test Users
    VALID_USERNAME = 'standard_user'
    VALID_PASSWORD = 'secret_sauce'
    LOCKED_USERNAME = 'locked_out_user'
    PROBLEM_USERNAME = 'problem_user'
    PERFORMANCE_USERNAME = 'performance_glitch_user'

    # Browser settings
    BROWSER = 'chrome'
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 20

    # Reporting
    SCREENSHOT_ON_FAILURE = True
    REPORT_PATH = 'reports/'

    # Test data
    TEST_DATA_PATH = 'testdata/'

    # Expected values
    EXPECTED_PRODUCT_COUNT = 6
    TAX_RATE = 0.08