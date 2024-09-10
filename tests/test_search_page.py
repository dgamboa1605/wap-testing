from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.streamer_page import StreamerPage
from utils import utils

class TestSearchPage:

    def test_search_streamer(self, browser):
        screenshot_path = f"{utils.get_root_path()}/data/screenshots/streamer.png"
        home_page = HomePage(browser)
        search_page = SearchPage(browser)
        streamer_page = StreamerPage(browser)


        home_page.click_on_search()
        search_page.search("StarCraft II")
        search_page.click_on_menu("Channels")
        search_page.load_more_streamers()
        search_page.select_streamer_randomly()
        streamer_page.is_loaded()
        streamer_page.take_screenshot(screenshot_path)

        assert streamer_page.is_file_present(screenshot_path), "Screenshot file does not exist."
