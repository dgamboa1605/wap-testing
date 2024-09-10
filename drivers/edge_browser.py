from drivers.browser import Browser
from selenium.webdriver.edge.options import Options
from selenium import webdriver

class EdgeBrowser(Browser):

    def get_driver(self):
        edge_options = Options()
        self._add_options(edge_options)
        return webdriver.Edge(options=edge_options)
    
    def _add_options(self, edge_options):
        if self.options:
            for option in self.options:
                edge_options.add_argument(option)
