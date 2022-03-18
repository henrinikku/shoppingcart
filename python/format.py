from abc import ABC, abstractmethod
from typing import List
from receipt import Receipt

class BaseFormatter(ABC):
    """
    Base class for all receipt line formatting implementations.
    
    Implementing classes receive a receipt and produce a list of lines (strings).
    E.g. some implementation might return a list of formatted items.
    """
    @abstractmethod
    def format(self, receipt: Receipt) -> List[str]:
        pass
