from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from browser import Browser

class ChromeBrowser(Browser):
    
    def get_driver(self):
        chrome_options = Options()
        self._add_options(chrome_options)
        return webdriver.Chrome(options=chrome_options)
    
    def _add_options(self, chrome_options):
        if self.options:
            for option in self.options:
                chrome_options.add_argument(option)
