from browser import Browser
from chrome_browser import ChromeBrowser
from firefox_browser import FirefoxBrowser
from edge_browser import EdgeBrowser

class BrowserFactory:
    
    @staticmethod
    def get_browser(self, browser_name: str, options=None) -> Browser:
        browsers = {
            "chrome": ChromeBrowser,
            "firefox": FirefoxBrowser,
            "edge": EdgeBrowser
        }

        if browser_name.lower() not in browsers:
            raise ValueError(f"Invalid browser name: {browser_name}")
        
        return browsers[browser_name.lower()](options)
