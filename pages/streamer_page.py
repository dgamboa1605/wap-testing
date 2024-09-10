from pages.base_page import BasePage
from drivers.browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class StreamerPage(BasePage):

    def __init__(self, driver: Browser) -> None:
        super().__init__(driver)
        self.loading_spinner = (By.CSS_SELECTOR, ".tw-loading-spinner")
        self.channel_status = (By.CSS_SELECTOR, ".tw-channel-status-text-indicator")

    def is_loaded(self):
        self.wait.until(EC.presence_of_element_located(self.channel_status))
        self.wait.until(EC.invisibility_of_element_located(self.loading_spinner))
