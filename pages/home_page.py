"""
Module providing basic actions on Home Page.
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from drivers.browser import Browser
from utilities.logger import Logger


class HomePage(BasePage):
    """
    HomePage class represents the homepage of the web application.
    This class inherits from BasePage and provides functionality specific to the homepage,
    such as interacting with the search input element.
    """
    logger = Logger(__name__)

    def __init__(self, driver: Browser) -> None:
        super().__init__(driver)
        self.search_input = (By.CSS_SELECTOR, "[aria-label='Search']")

    def click_on_search(self) -> None:
        """
        Clicks on the search input field on the homepage.

        This method uses the locator for the search input field and triggers a click event on it.
        """
        try:
            self.logger.info("Attempting to click on the search input")
            self.click(self.search_input)
            self.logger.info("Successfully clicked on the search input")
        except Exception as e:
            self.logger.error(f"Failed to click on the search input: {e}")
            raise
