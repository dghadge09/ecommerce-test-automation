"""
Base Page with common methods for all pages
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.logger = logging.getLogger(__name__)

    def find_element(self, locator):
        """Find element with wait"""
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException:
            self.logger.error(f"Element not found: {locator}")
            raise

    def click(self, locator):
        """Click element"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def enter_text(self, locator, text):
        """Enter text in field"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Get element text"""
        element = self.find_element(locator)
        return element.text

    def is_element_visible(self, locator, timeout=10):
        """Check if element is visible"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def take_screenshot(self, name):
        """Take screenshot"""
        self.driver.save_screenshot(f"reports/screenshots/{name}.png")