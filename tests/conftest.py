"""
Module tear down.
"""
from typing import Any
import pytest

from drivers.browser_factory import BrowserFactory
from config import config
from utilities.logger import Logger

logger = Logger(__name__)


@pytest.fixture(scope="function")
def browser() -> Any:
    """
    Fixture to set up and tear down a web browser instance for tests.

    This fixture initializes a web browser instance using the BrowserFactory
    and navigates to the URL specified in the configuration. After the test
    completes, the browser instance is closed.

    Returns:
        WebDriver: An instance of the web browser driver.
    """
    logger.info("Setting up the web browser instance.")

    try:
        driver = BrowserFactory.get_browser(
            config.BROWSER, config.CHROME_OPTIONS).get_driver()
        logger.info(f"Browser initialized with URL: {config.URL}")
        driver.get(config.URL)
        yield driver
    except Exception as e:
        logger.error(f"An error occurred while setting up the browser: {e}")
        raise
    finally:
        if 'driver' in locals():
            driver.quit()
            logger.info("Browser instance closed.")
