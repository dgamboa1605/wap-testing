
"""
A configuration class for setting up the browser and test environment.

BROWSER (str): The browser to be used for running tests. Default is "chrome".
URL (str): The base URL of the application under test. Default is the Twitch mobile site.
BROWSER_OPTIONS (list): A list of additional options for configuring Chrome browser behavior. 
                        Default is an empty list. (e.g. ["mobileEmulation", "--headless"])
DEVICE_NAME (str): The device name to be used to simulate a mobile. (e.g. 'iPhone SE', 
                    'iPhone 12 Pro', 'Pixel 4', 'Nexus 6')
IMPLICIT_WAIT (int): The time (in seconds) to wait for elements to be found implicitly. 
                        Default is 3 seconds.
EXPLICIT_WAIT (int): The time (in seconds) to wait for elements to be found explicitly 
                        using WebDriverWait. Default is 10 seconds.
LOG_LEVEL (str): The level of logging to be used (e.g., DEBUG, INFO). Default is "DEBUG".
LOG_NAME (str): The name of the log file.
"""

BROWSER = "chrome"
URL = "https://m.twitch.tv/"
BROWSER_OPTIONS = ["mobileEmulation"]
DEVICE_NAME = "iPhone X"
IMPLICIT_WAIT = 4
EXPLICIT_WAIT = 10
LOG_LEVEL = "DEBUG"
LOG_NAME = "log_file.log"
