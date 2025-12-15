"""
Pytest configuration and fixtures - Using local ChromeDriver
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from config.config import Config
import logging
import os
import sys

@pytest.fixture(scope="function")
def driver():
    """
    Setup and teardown browser driver using local ChromeDriver
    """
    # Chrome options for headless execution
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-popup-blocking")
    
    # ChromeDriver path (downloaded by Jenkins build script)
    driver_path = os.path.join(os.getcwd(), "drivers", "chromedriver.exe")
    
    print(f"Current directory: {os.getcwd()}")
    print(f"Looking for ChromeDriver at: {driver_path}")
    
    if not os.path.exists(driver_path):
        raise FileNotFoundError(f"ChromeDriver not found at: {driver_path}")
    
    try:
        # Create service and driver
        service = Service(executable_path=driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # Set implicit wait
        driver.implicitly_wait(Config.IMPLICIT_WAIT)
        
        # Navigate to application
        print(f"Navigating to: {Config.BASE_URL}")
        driver.get(Config.BASE_URL)
        print(f"Current URL: {driver.current_url}")
        print(f"Page title: {driver.title}")
        
        yield driver
        
        # Teardown
        print("Closing browser...")
        driver.quit()
        
    except Exception as e:
        print(f"ERROR creating driver: {e}")
        print(f"Python version: {sys.version}")
        print(f"Driver path checked: {driver_path}")
        import traceback
        traceback.print_exc()
        raise

@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    """
    Configure logging for test execution
    """
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
    Take screenshot when test fails
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
