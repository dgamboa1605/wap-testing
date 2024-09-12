"""
Module Edge configurations.
"""
from selenium.webdriver.edge.options import Options
from selenium import webdriver
from drivers.browser import Browser
from utilities.logger import Logger


class EdgeBrowser(Browser):
    """
    A class to manage the Edge browser for Selenium WebDriver with custom options.

    This class inherits from the `Browser` class and is used to create a Selenium WebDriver
    instance for Edge with specific options.
    """
    logger = Logger(__name__)

    def get_driver(self) -> webdriver.Edge:
        """
        Initializes and returns a Edge WebDriver instance with the provided options.

        Returns:
            webdriver.Edge: A WebDriver instance for Edge with the applied options.
        """
        try:
            self.logger.info("Initializing Edge WebDriver")
            edge_options = Options()
            self._add_options(edge_options)
            self.logger.info("Edge WebDriver successfully initialized")
            return webdriver.Edge(options=edge_options)
        except Exception as e:
            self.logger.error(f"Failed to initialize Edge WebDriver: {str(e)}")
            raise

    def _add_options(self, edge_options: Options) -> None:
        """
        Adds custom options to the Edge WebDriver instance based on the `self.options` attribute.

        Args:
            edge_options (Options): The Options instance to which the arguments should 
            be added.
        """
        try:
            if self.options:
                self.logger.info("Adding Edge options")
                for option in self.options:
                    self.logger.debug(f"Added option: {option}")
                    edge_options.add_argument(option)
                self.logger.info("All Edge options added successfully")
            else:
                self.logger.warning("No options provided for Edge WebDriver")
        except Exception as e:
            self.logger.error(f"Error while adding Edge options: {str(e)}")
            raise
