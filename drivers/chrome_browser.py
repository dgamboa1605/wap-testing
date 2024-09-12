"""
Module Chrome configurations.
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from drivers.browser import Browser
from utilities.logger import Logger


class ChromeBrowser(Browser):
    """
    A class to manage the Chrome browser for Selenium WebDriver with custom options.

    This class inherits from the `Browser` class and is used to create a Selenium WebDriver
    instance for Chrome with specific options.
    """
    logger = Logger(__name__)

    def get_driver(self) -> webdriver.Chrome:
        """
        Initializes and returns a Chrome WebDriver instance with the provided options.

        Returns:
            webdriver.Chrome: A WebDriver instance for Chrome with the applied options.
        """
        try:
            self.logger.info("Initializing Chrome WebDriver")
            chrome_options = Options()
            self._add_options(chrome_options)
            self.logger.info("Chrome WebDriver successfully initialized")
            return webdriver.Chrome(options=chrome_options)
        except Exception as e:
            self.logger.error(f"Failed to initialize Chrome WebDriver: {str(e)}")
            raise

    def _add_options(self, chrome_options: Options) -> None:
        """
        Adds custom options to the Chrome WebDriver instance based on the `self.options` attribute.

        Args:
            chrome_options (Options): An instance of Chrome options to which arguments 
            will be added. (selenium.webdriver.chrome.options.Options)
        """
        try:
            if self.options:
                self.logger.info("Adding Chrome options")
                for option in self.options:
                    self.logger.debug(f"Added option: {option}")
                    chrome_options.add_argument(option)
                self.logger.info("All Chrome options added successfully")
            else:
                self.logger.warning("No options provided for Chrome WebDriver")
        except Exception as e:
            self.logger.error(f"Error while adding Chrome options: {str(e)}")
            raise
