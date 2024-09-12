"""
Module Browser interface.
"""
from abc import ABC, abstractmethod
from typing import Any


class Browser(ABC):
    """
    An abstract base class for a browser. This class defines the interface 
    for any browser that needs to provide a web driver.

    Attributes:
        options: Optional settings or configurations for the browser.
    """

    def __init__(self, options=None) -> None:
        self.options = options

    @abstractmethod
    def get_driver(self) -> Any:
        """
        Abstract method to retrieve the web driver. This method must be 
        implemented by any subclass inheriting from the Browser class.

        Returns:
            A web driver instance configured with the browser's options.
        """

    def set_options(self, options: Any) -> None:
        """
        Sets the options for the browser.

        Args:
            options: New settings or configurations for the browser.
        """
        self.options = options
