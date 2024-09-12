"""
Module providing basic actions of a page.
"""
import os
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebElement
from drivers.browser import Browser
from config import config
from utilities.logger import Logger


class BasePage:
    """
    Class representing basic actions of a page.

    Attributes:
        driver: An instance of the Selenium WebDriver.
        wait: An instance of WebDriverWait for managing wait conditions.
    """
    logger = Logger(__name__)

    def __init__(self, driver: Browser) -> None:
        self.driver = driver
        self.wait = WebDriverWait(self.driver, config.EXPLICIT_WAIT)

    def find_element(self, locator: tuple) -> WebElement:
        """
        Find a single element on the page by its locator.

        Args:
            locator (tuple): A tuple representing the locator strategy and value
            (e.g., (By.ID, 'element_id')).

        Returns:
            WebElement: The WebElement that is visible and located by the provided locator.
        """
        self.logger.info(f"Attempting to find element with locator: {locator}")
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            self.logger.info(f"Element found with locator: {locator}")
            return element
        except Exception as e:
            self.logger.error(f"Error finding element with locator {locator}: {e}")
            raise

    def find_elements(self, locator: tuple) -> WebElement:
        """
        Find multiple elements on the page by their locator.

        Args:
            locator (tuple): A tuple representing the locator strategy and value
            (e.g., (By.ID, 'element_id')).

        Returns:
            list: A list of WebElements that are visible and located by the provided locator.
        """
        self.logger.info(f"Attempting to find elements with locator: {locator}")
        try:
            elements = self.wait.until(EC.visibility_of_all_elements_located(locator))
            self.logger.info(f"Elements found with locator: {locator}")
            return elements
        except Exception as e:
            self.logger.error(f"Error finding elements with locator {locator}: {e}")
            raise

    def click(self, locator: tuple) -> None:
        """
        Click on an element located by the provided locator.

        Args:
            locator (tuple): A tuple representing the locator strategy and value 
            (e.g., (By.ID, 'element_id')).
        """
        self.logger.info(f"Attempting to click element with locator: {locator}")
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            self.logger.info(f"Clicked element with locator: {locator}")
        except Exception as e:
            self.logger.error(f"Error clicking element with locator {locator}: {e}")
            raise

    def send_keys(self, locator: tuple, text: str, key=None) -> None:
        """
        Send keys to an input element located by the provided locator.

        Args:
            locator (tuple): A tuple representing the locator strategy and value 
            (e.g., (By.ID, 'element_id')).
            text (str): The text to be sent to the input element.
            key (Keys): Optional selenium common keys value (e.g., Keys.ENTER, Keys.TAB). 
            If provided, this key will be pressed after sending the text.
        """
        self.logger.info(f"Attempting to send keys to element with locator: {locator}")
        try:
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)
            self.logger.info(f"Sent text '{text}' to element with locator: {locator}")
            if key:
                element.send_keys(key)
        except Exception as e:
            self.logger.error(f"Error sending keys to element with locator {locator}: {e}")
            raise

    def get_text(self, locator: tuple) -> str:
        """
        Get the text content of an element located by the provided locator.

        Args:
            locator (tuple): A tuple representing the locator strategy and value 
            (e.g., (By.ID, 'element_id')).

        Returns:
            str: The text content of the WebElement.
        """
        self.logger.info(f"Attempting to get text from element with locator: {locator}")
        try:
            text = self.find_element(locator).text
            self.logger.info(f"Text '{text}' retrieved from element with locator: {locator}")
            return text
        except Exception as e:
            self.logger.error(f"Error getting text from element with locator {locator}: {e}")
            raise

    def scroll_down(self) -> None:
        """
        Scroll down the page to the bottom.
        """
        self.logger.info("Scrolling down the page.")
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.logger.info("Scrolled to the bottom of the page.")
        except Exception as e:
            self.logger.error(f"Error scrolling down the page: {e}")
            raise

    def wait_for_page_to_load(self) -> None:
        """
        Wait for the page to fully load and be ready for interaction.

        The method waits until the document.readyState is 'complete' and applies an implicit wait.
        """
        self.logger.info("Waiting for the page to fully load.")
        try:
            self.wait.until(lambda d: d.execute_script('return document.readyState') == 'complete')
            self.driver.implicitly_wait(config.IMPLICIT_WAIT)
            time.sleep(config.IMPLICIT_WAIT)
            self.logger.info("Page fully loaded.")
        except Exception as e:
            self.logger.error(f"Error waiting for page to load: {e}")
            raise

    def take_screenshot(self, file_path: str) -> bool:
        """
        Take a screenshot of the current page and save it to the specified file path.

        Args:
            file_path (str): The path where the screenshot will be saved.

        Returns:
            bool: True if the screenshot was successfully saved, otherwise False.
        """
        self.logger.info(f"Attempting to take a screenshot and save to: {file_path}")
        try:
            success = self.driver.save_screenshot(file_path)
            if success:
                self.logger.info(f"Screenshot saved to: {file_path}")
            else:
                self.logger.warning(f"Failed to save screenshot to: {file_path}")
            return success
        except Exception as e:
            self.logger.error(f"Error taking screenshot: {e}")
            raise

    def is_file_present(self, file_path: str) -> bool:
        """
        Check if a file exists at the given file path.

        Args:
            file_path (str): The path to the file to check.

        Returns:
            bool: True if the file exists, otherwise False.
        """
        self.logger.info(f"Checking if file exists at: {file_path}")
        try:
            file_exists = os.path.exists(file_path)
            if file_exists:
                self.logger.info(f"File exists at: {file_path}")
            else:
                self.logger.warning(f"File not found at: {file_path}")
            return file_exists
        except Exception as e:
            self.logger.error(f"Error checking file presence at {file_path}: {e}")
            raise
