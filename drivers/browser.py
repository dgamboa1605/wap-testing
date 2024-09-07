from abc import ABC, abstractmethod

class Browser(ABC):
    
    def __init__(self, options=None) -> None:
        self.options = options
    
    @abstractmethod
    def get_driver(self):
        """Abstract method to be implemented by concrete browsers."""
        pass
