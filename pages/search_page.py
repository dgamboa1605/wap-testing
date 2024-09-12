"""
Module providing basic actions on Search Page.
"""
import random

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from drivers.browser import Browser
from utilities.logger import Logger


class SearchPage(BasePage):
    """
    SearchPage class represents the page for searching streamers and 
    interacting with search results.

    This class inherits from BasePage and provides methods to perform search operations,
    click on menu options, select streamers randomly, and load more streamer results.
    """
    logger = Logger(__name__)

    def __init__(self, driver: Browser) -> None:
        super().__init__(driver)
        self.input_search = (By.CSS_SELECTOR, "[data-a-target='tw-input']")
        self.streamers = (By.CSS_SELECTOR, "[role='list']>div")
        self.image = (By.CSS_SELECTOR,  "img.tw-image")

    def search(self, text: str) -> None:
        """
        Performs a search by typing the provided text into the search input field
        and submitting it by pressing Enter.

        Args:
            text (str): The text to search for.
        """
        self.logger.info(f"Starting search for: {text}")
        try:
            self.send_keys(self.input_search, text, Keys.ENTER)
            self.logger.info(f"Search submitted for: {text}")
        except Exception as e:
            self.logger.error(f"Error occurred during search: {e}")
            raise

    def click_on_menu(self, option: str) -> None:
        """
        Clicks on a specific menu option based on the provided option text.

        Args:
            option (str): The menu option text to click on.
        """
        locator = f"//div[contains(text(), '{option}')]"
        self.logger.info(f"Attempting to click on menu option: {option}")
        try:
            self.click((By.XPATH, locator))
            self.logger.info(f"Menu option clicked: {option}")
        except Exception as e:
            self.logger.error(
                f"Error occurred while clicking menu option '{option}': {e}")
            raise

    def select_streamer_randomly(self) -> None:
        """
        Selects a streamer randomly from the list of streamers displayed on the page.

        Waits for the list of streamers to be present and then randomly selects
        one that is clickable.
        """
        self.logger.info("Selecting a streamer randomly.")
        try:
            streamers = self.wait.until(
                EC.visibility_of_all_elements_located(self.streamers))
            num_streamers = len(streamers)
            if num_streamers == 0:
                self.logger.warning("No streamers found to select.")
                return
            random_index = random.randint(0, num_streamers - 1)
            element = self.wait.until(
                EC.element_to_be_clickable(streamers[random_index]))
            self.click(element)
            self.logger.info(f"Streamer at index {random_index} selected.")
        except Exception as e:
            self.logger.error(
                f"Error occurred while selecting a streamer: {e}")
            raise

    def load_more_streamers(self, max_scrolls: int = 1, current_scroll: int = 0) -> None:
        """
        Scrolls down the page to load more streamers. This method performs
        recursive scrolling until the maximum number of scrolls is reached.

        Args:
            max_scrolls (int): The maximum number of scrolls to perform. Default is 2.
            current_scroll (int): The current scroll count during the recursion. Default is 0.
        """
        if current_scroll >= max_scrolls:
            self.logger.info("Maximum scroll limit reached.")
            return

        self.logger.info(
            f"Scrolling down. Current scroll count: {current_scroll}")
        try:
            self.wait_for_page_to_load()
            self.scroll_down()
            self.load_more_streamers(max_scrolls, current_scroll + 1)
        except Exception as e:
            self.logger.error(f"Error occurred while scrolling down: {e}")
            raise
