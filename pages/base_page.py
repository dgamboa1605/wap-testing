import os
import time

from drivers.browser import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver: Browser) -> None:
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
    
    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def find_elements(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))
    
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def send_keys(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
        element.send_keys(Keys.ENTER)
    
    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def wait_for_page_to_load(self):
        self.wait.until(lambda d: d.execute_script('return document.readyState') == 'complete')
        time.sleep(3)
        #TODO add validation to wait until images are downloaded

    def take_screenshot(self, file_path: str) -> bool:
        """Take a screenshot of the current page and save it to the specified file path."""
        return self.driver.save_screenshot(file_path)

    def is_file_present(self, file_path: str) -> bool:
        """Check if a file exists at the given file path."""
        return os.path.exists(file_path)
