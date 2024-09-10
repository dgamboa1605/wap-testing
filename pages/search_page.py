import random

from pages.base_page import BasePage
from drivers.browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class SearchPage(BasePage):

    def __init__(self, driver: Browser) -> None:
        super().__init__(driver)
        self.input_search = (By.CSS_SELECTOR, "[data-a-target='tw-input']")
        self.streamers = (By.CSS_SELECTOR, "[role='list']>div")
        self.image = (By.CSS_SELECTOR,  "img.tw-image")

    def search(self, text):
        self.send_keys(self.input_search, text)
    
    def click_on_menu(self, option):
        locator = f"//div[contains(text(), '{option}')]"
        self.click((By.XPATH, locator))

    def select_streamer_randomly(self):
        streamers = self.wait.until(EC.presence_of_all_elements_located(self.streamers))
        num_streamers = len(streamers)
        random_index = random.randint(0, num_streamers - 1)
        element = self.wait.until(EC.element_to_be_clickable(streamers[random_index]))
        self.click(element)
    
    def load_more_streamers(self, max_scrolls=2, current_scroll=0):
        if current_scroll >= max_scrolls:
            return
        self.scroll_down()
        self.wait_for_page_to_load()
        self.load_more_streamers(max_scrolls, current_scroll + 1)
