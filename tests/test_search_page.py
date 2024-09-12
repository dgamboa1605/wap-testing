"""
Module test search page.
"""
import pytest
import allure

from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.streamer_page import StreamerPage
from utilities import utils
from utilities.logger import Logger


@pytest.mark.usefixtures("browser")
class TestSearchPage:
    """
    Test class for the Search Page functionality in the application.
    It sets up the necessary pages and contains tests related to the 
    search functionality and streamer page.
    """

    home_page: HomePage = None
    search_page: SearchPage = None
    streamer_page: StreamerPage = None
    logger = Logger(__name__)

    @pytest.fixture(autouse=True)
    def setup(self, browser) -> None:
        """
        Fixture to set up the pages before each test is run.

        Args:
            browser: The browser instance to be used for the tests.
        """
        self.home_page = HomePage(browser)
        self.search_page = SearchPage(browser)
        self.streamer_page = StreamerPage(browser)

    @allure.title("Take Screenshot of a Streamer")
    @allure.description(
        "Test case to take a screenshot of a randomly selected streamer.\n"
        "1. Clicks on the search button on the home page.\n"
        "2. Searches for 'StarCraft II' on the search page.\n"
        "3. Selects the 'Channels' tab.\n"
        "4. Loads more streamers.\n"
        "5. Selects a streamer randomly.\n"
        "6. Takes a screenshot of the streamer page.\n"
        "7. Asserts that the screenshot file is created."
    )
    def test_take_screenshot_to_streamer(self):
        """
        Test case to take a screenshot of a randomly selected streamer.

        Raises:
            AssertionError: If the screenshot file does not exist.
        """
        self.logger.info("Starting test: test_take_screenshot_to_streamer")
        screenshot_path = f"{utils.get_root_path()}/data/screenshots/streamer.png"

        self.home_page.click_on_search()
        self.search_page.search("StarCraft II")
        self.search_page.click_on_menu("Channels")
        self.search_page.load_more_streamers(max_scrolls=2)
        self.search_page.select_streamer_randomly()
        self.streamer_page.is_loaded()
        self.streamer_page.take_screenshot(screenshot_path)

        assert self.streamer_page.is_file_present(
            screenshot_path), "Screenshot file does not exist."
        self.logger.info("Ending test: test_take_screenshot_to_streamer")
