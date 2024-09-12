"""
Module providing basic actions on Streamer Page.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from drivers.browser import Browser
from utilities.logger import Logger


class StreamerPage(BasePage):
    """
    StreamerPage represents a page object model for a streamer's channel page. 
    This class provides methods to interact with and validate the state of 
    the channel's loading status.
    """
    logger = Logger(__name__)

    def __init__(self, driver: Browser) -> None:
        super().__init__(driver)
        self.loading_spinner = (By.CSS_SELECTOR, ".tw-loading-spinner")
        self.channel_status = (
            By.CSS_SELECTOR, ".tw-channel-status-text-indicator")

    def is_loaded(self) -> None:
        """
        Waits until the page is fully loaded by checking for the presence of
        the channel status element and ensuring the loading spinner is no longer visible.
        """
        self.logger.info("Checking if the StreamerPage is loaded.")

        try:
            self.logger.debug(
                "Waiting for the channel status element to be present.")
            self.wait.until(
                EC.presence_of_element_located(self.channel_status))

            self.logger.debug("Waiting for the loading spinner to disappear.")
            self.wait.until(
                EC.invisibility_of_element_located(self.loading_spinner))

            self.logger.info("StreamerPage has been successfully loaded.")
        except Exception as e:
            self.logger.error(
                f"An error occurred while checking if the StreamerPage is loaded: {e}")
            raise
