"""
Products Page Object Model
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductsPage(BasePage):
    # Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    
    def is_products_page_displayed(self):
        """Verify we're on products page"""
        return self.is_element_visible(self.PAGE_TITLE)
    
    def get_page_title(self):
        """Get page title text"""
        return self.get_text(self.PAGE_TITLE)
    
    def get_product_count(self):
        """Get number of products"""
        products = self.driver.find_elements(*self.INVENTORY_ITEMS)
        return len(products)
