
"""
A configuration class for setting up the browser and test environment.

Attributes:
    BROWSER (str): The browser to be used for running tests. Default is "chrome".
    URL (str): The base URL of the application under test. Default is the Twitch mobile site.
    CHROME_OPTIONS (list): A list of additional options for configuring Chrome browser behavior. 
                            Default is an empty list.
    IMPLICIT_WAIT (int): The time (in seconds) to wait for elements to be found implicitly. 
                            Default is 3 seconds.
    EXPLICIT_WAIT (int): The time (in seconds) to wait for elements to be found explicitly 
                            using WebDriverWait. Default is 10 seconds.
    LOG_LEVEL (str): The level of logging to be used (e.g., DEBUG, INFO). Default is "DEBUG".
    LOG_NAME (str): The name of the log file.
"""

BROWSER = "chrome"
URL = "https://m.twitch.tv/"
CHROME_OPTIONS = []
IMPLICIT_WAIT = 3
EXPLICIT_WAIT = 10
LOG_LEVEL = "DEBUG"
LOG_NAME = "log_file.log"
