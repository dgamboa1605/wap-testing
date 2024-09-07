from drivers.browser import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver: Browser) -> None:
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
    
    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def send_keys(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text
