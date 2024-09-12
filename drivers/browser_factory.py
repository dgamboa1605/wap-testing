"""
Module providing a function to get type of browser.
"""
from typing import List
from drivers.chrome_browser import ChromeBrowser
from drivers.firefox_browser import FirefoxBrowser
from drivers.edge_browser import EdgeBrowser
from drivers.browser import Browser
from utilities.logger import Logger


class BrowserFactory:
    """
    A factory class to initialize web browser drivers based on the given browser name.

    The class supports Chrome, Firefox, and Edge browsers. It provides a static method 
    to return an instance of the selected browser's driver.

    Usage:
        browser_instance = BrowserFactory.get_browser("chrome", options)
    """
    logger = Logger(__name__)

    @staticmethod
    def get_browser(browser_name: str, options: List[str] = None) -> Browser:
        """
        Returns an instance of a browser driver based on the provided browser name.

        Args:
            browser_name (str): The name of the browser to initialize. Accepted values 
                                are "chrome", "firefox", or "edge".
            options (List[str]): Optional browser-specific settings or options to 
                                pass when initializing the browser driver.
                                (e.g. ['--headless','--disable-gpu', '--window-size=1200x800'])

        Returns:
            object: An instance of the browser driver corresponding to the given browser name.

        Raises:
            ValueError: If the browser name provided is not supported (e.g., not "chrome", 
                        "firefox", or "edge").

        Example:
            chrome_driver = BrowserFactory.get_browser("chrome", options)
            firefox_driver = BrowserFactory.get_browser("firefox")
        """
        BrowserFactory.logger.info(
            f"Attempting to initialize browser: {browser_name} with options: {options}")
        browsers = {
            "chrome": ChromeBrowser,
            "firefox": FirefoxBrowser,
            "edge": EdgeBrowser
        }
        if browser_name.lower() not in browsers:
            BrowserFactory.logger.error(
                f"Invalid browser name: {browser_name}")
            raise ValueError(f"Invalid browser name: {browser_name}")

        BrowserFactory.logger.info(
            f"Successfully initialized {browser_name} browser.")
        return browsers[browser_name.lower()](options)

    @staticmethod
    def is_valid_browser(browser_name: str) -> bool:
        """
        Checks if the given browser name is valid.

        Args:
            browser_name (str): The name of the browser to validate.

        Returns:
            bool: True if the browser name is valid, False otherwise.
        """
        BrowserFactory.logger.debug(f"Validating browser name: {browser_name}")
        valid_browsers = ["chrome", "firefox", "edge"]
        is_valid = browser_name.lower() in valid_browsers
        if is_valid:
            BrowserFactory.logger.info(
                f"Browser name '{browser_name}' is valid.")
        else:
            BrowserFactory.logger.warning(
                f"Browser name '{browser_name}' is invalid.")
        return is_valid
