from abc import ABC, abstractmethod
from item import Item


class BaseItemFormatter(ABC):
    """
    Base class for item formatting implementations.
    """

    @abstractmethod
    def format_item(self, item: Item):
        pass


class PriceFirstItemFormatter(BaseItemFormatter):
    """
    Item formatting implementation that shows the price first.
    """

    def format_item(self, item: Item):
        return f"{item.price} - {item.name} - {item.count}"


class PriceLastItemFormatter(BaseItemFormatter):
    """
    Item formatting implementation that shows the price last.
    """

    def format_item(self, item: Item):
        return f"{item.name} - {item.count} - {item.price}"
