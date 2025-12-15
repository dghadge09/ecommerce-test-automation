"""
Pytest configuration and fixtures
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from config.config import Config
import logging
import os

@pytest.fixture(scope="function")
def driver():
    """
    Setup and teardown browser driver for each test
    """
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Create driver with webdriver_manager
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.implicitly_wait(Config.IMPLICIT_WAIT)
        driver.get(Config.BASE_URL)
        
        yield driver
        
        # Teardown
        driver.quit()
        
    except Exception as e:
        print(f"Error creating driver: {e}")
        raise

@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    """
    Configure logging for test execution
    """
    # Create reports directory if it doesn't exist
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
    """
    Take screenshot automatically when a test fails
    """
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        driver = item.funcargs.get('driver')
        if driver:
            try:
                screenshot_name = f"{item.name}_{call.when}"
                driver.save_screenshot(f"reports/screenshots/{screenshot_name}.png")
                print(f"Screenshot saved: {screenshot_name}.png")
            except Exception as e:
                print(f"Failed to take screenshot: {e}")
