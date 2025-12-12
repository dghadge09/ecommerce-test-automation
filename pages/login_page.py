"""
Login Page Object Model
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def enter_username(self, username):
        """Enter username"""
        self.logger.info(f"Entering username: {username}")
        self.enter_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        """Enter password"""
        self.logger.info("Entering password")
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_login_button(self):
        """Click login button"""
        self.logger.info("Clicking login button")
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        """Complete login flow"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def is_error_displayed(self):
        """Check if error is visible"""
        return self.is_element_visible(self.ERROR_MESSAGE, timeout=5)

    def get_error_message(self):
        """Get error message text"""
        return self.get_text(self.ERROR_MESSAGE)