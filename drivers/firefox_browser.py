from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from browser import Browser

class FirefoxBrowser(Browser):

    def get_driver(self):
        firefox_options = Options()
        self._add_options(firefox_options)
        return webdriver.Firefox(options=firefox_options)
    
    def _add_options(self, firefox_options):
        if self.options:
            for option in self.options:
                firefox_options.add_argument(option)
