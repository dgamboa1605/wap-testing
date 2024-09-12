"""
Module FireFox configurations.
"""
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from drivers.browser import Browser
from utilities.logger import Logger


class FirefoxBrowser(Browser):
    """
    A class to manage the FireFox browser for Selenium WebDriver with custom options.

    This class inherits from the `Browser` class and is used to create a Selenium WebDriver
    instance for FireFox with specific options.
    """
    logger = Logger(__name__)

    def get_driver(self) -> webdriver.Firefox:
        """
        Initializes and returns a FireFox WebDriver instance with the provided options.

        Returns:
            webdriver.FireFox: A WebDriver instance for FireFox with the applied options.
        """
        try:
            self.logger.info("Initializing FireFox WebDriver")
            firefox_options = Options()
            self._add_options(firefox_options)
            self.logger.info("FireFox WebDriver successfully initialized")
            return webdriver.Firefox(options=firefox_options)
        except Exception as e:
            self.logger.error(f"Failed to initialize FireFox WebDriver: {str(e)}")
            raise

    def _add_options(self, firefox_options: Options) -> None:
        """
        Adds custom options to the Firefox WebDriver instance based on the `self.options` attribute.

        Args:
            firefox_options (Options): An instance of Firefox options to which arguments 
            will be added.
        """
        try:
            if self.options:
                self.logger.info("Adding FireFox options")
                for option in self.options:
                    firefox_options.add_argument(option)
                    self.logger.debug(f"Added option: {option}")
                self.logger.info("All FireFox options added successfully")
            else:
                self.logger.warning("No options provided for FireFox WebDriver")
        except Exception as e:
            self.logger.error(f"Error while adding FireFox options: {str(e)}")
            raise
