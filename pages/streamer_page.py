from base_page import BasePage
from drivers.browser import Browser


class StreamerPage(BasePage):

    def __init__(self, driver: Browser) -> None:
        super().__init__(driver)
