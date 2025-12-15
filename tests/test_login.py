"""
Login functionality test cases
"""
import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from config.config import Config

class TestLogin:
    
    def test_successful_login_standard_user(self, driver):
        """Test successful login with valid credentials"""
        login_page = LoginPage(driver)
        products_page = ProductsPage(driver)
        
        # Perform login
        login_page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)
        
        # Verify success
        assert products_page.is_products_page_displayed(), "Products page not displayed"
        assert products_page.get_page_title() == "Products", "Incorrect page title"
        print("PASS: Standard user logged in successfully")
    
    def test_locked_user_login(self, driver):
        """Test login with locked user"""
        login_page = LoginPage(driver)
        
        login_page.login(Config.LOCKED_USERNAME, Config.VALID_PASSWORD)
        
        assert login_page.is_error_displayed(), "Error message not displayed"
        error_text = login_page.get_error_message()
        assert "locked out" in error_text.lower(), f"Unexpected error: {error_text}"
        print("PASS: Locked user error shown correctly")
    
    def test_invalid_credentials(self, driver):
        """Test login with invalid credentials"""
        login_page = LoginPage(driver)
        
        login_page.login("invalid_user", "invalid_password")
        
        assert login_page.is_error_displayed(), "Error message not displayed"
        print("PASS: Invalid credentials error shown correctly")
    
    def test_empty_username(self, driver):
        """Test login with empty username"""
        login_page = LoginPage(driver)
        
        login_page.login("", Config.VALID_PASSWORD)
        
        assert login_page.is_error_displayed(), "Error message not displayed"
        error_text = login_page.get_error_message()
        assert "username is required" in error_text.lower(), f"Unexpected error: {error_text}"
        print("PASS: Empty username error shown correctly")
    
    def test_empty_password(self, driver):
        """Test login with empty password"""
        login_page = LoginPage(driver)
        
        login_page.login(Config.VALID_USERNAME, "")
        
        assert login_page.is_error_displayed(), "Error message not displayed"
        error_text = login_page.get_error_message()
        assert "password is required" in error_text.lower(), f"Unexpected error: {error_text}"
        print("PASS: Empty password error shown correctly")
