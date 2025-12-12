"""
Pytest configuration and fixtures
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config.config import Config
import logging
import os


@pytest.fixture(scope="function")
def driver():
    """Setup and teardown browser driver"""
    # Setup
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(Config.IMPLICIT_WAIT)
    driver.get(Config.BASE_URL)

    yield driver

    # Teardown
    driver.quit()


@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    """Configure logging"""
    os.makedirs('reports', exist_ok=True)
    os.makedirs('reports/screenshots', exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('reports/test_execution.log'),
            logging.StreamHandler()
        ]
    )


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Take screenshot on test failure"""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get('driver')
        if driver:
            screenshot_name = f"{item.name}_{call.when}"
            driver.save_screenshot(f"reports/screenshots/{screenshot_name}.png")