"""
Login functionality test cases
Tests various login scenarios
"""
import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from config.config import Config


class TestLogin:
    """Group of login-related tests"""

    def test_successful_login_standard_user(self, driver):
        """
        Test Case: Verify successful login with valid credentials
        Expected: User should see products page
        """
        # Arrange - create page objects
        login_page = LoginPage(driver)
        products_page = ProductsPage(driver)

        # Act - perform login
        login_page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)

        # Assert - verify results
        assert products_page.is_products_page_displayed(), "Products page not displayed after login"
        assert products_page.get_page_title() == "Products", "Page title is incorrect"
        print("✅ Test Passed: Standard user logged in successfully")

    def test_locked_out_user_login(self, driver):
        """
        Test Case: Verify error message for locked out user
        Expected: Error message should be displayed
        """
        login_page = LoginPage(driver)

        # Attempt login with locked user
        login_page.login(Config.LOCKED_USERNAME, Config.VALID_PASSWORD)

        # Verify error is displayed
        assert login_page.is_error_displayed(), "Error message not displayed for locked user"

        error_text = login_page.get_error_message()
        assert "locked out" in error_text.lower(), f"Unexpected error message: {error_text}"
        print(f"✅ Test Passed: Locked user error shown: {error_text}")

    def test_invalid_username(self, driver):
        """
        Test Case: Login with invalid username
        Expected: Error message about incorrect credentials
        """
        login_page = LoginPage(driver)

        login_page.login("invalid_user", Config.VALID_PASSWORD)

        assert login_page.is_error_displayed(), "Error message not displayed"
        error_text = login_page.get_error_message()
        assert "do not match" in error_text.lower(), f"Unexpected error: {error_text}"
        print("✅ Test Passed: Invalid username error shown")

    def test_empty_username(self, driver):
        """
        Test Case: Login with empty username
        Expected: Error message about required username
        """
        login_page = LoginPage(driver)

        login_page.login("", Config.VALID_PASSWORD)

        assert login_page.is_error_displayed(), "Error message not displayed"
        error_text = login_page.get_error_message()
        assert "username is required" in error_text.lower(), f"Unexpected error: {error_text}"
        print("✅ Test Passed: Empty username error shown")

    def test_empty_password(self, driver):
        """
        Test Case: Login with empty password
        Expected: Error message about required password
        """
        login_page = LoginPage(driver)

        login_page.login(Config.VALID_USERNAME, "")

        assert login_page.is_error_displayed(), "Error message not displayed"
        error_text = login_page.get_error_message()
        assert "password is required" in error_text.lower(), f"Unexpected error: {error_text}"
        print("✅ Test Passed: Empty password error shown")