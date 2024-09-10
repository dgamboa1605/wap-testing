import pytest

from drivers.browser_factory import BrowserFactory
from config import config

@pytest.fixture
def browser():
    browser = BrowserFactory.get_browser(config.BROWSER, config.CHROME_OPTIONS)
    driver = browser.get_driver()
    driver.get(config.URL)
    yield driver
    driver.quit()
