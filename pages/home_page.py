from pages.base_page import BasePage
from drivers.browser import Browser
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    def __init__(self, driver: Browser) -> None:
        super().__init__(driver)
        self.search_input = (By.CSS_SELECTOR, "[aria-label='Search']")
    
    def click_on_search(self):
        self.click(self.search_input)
