from abc import abstractmethod

from item import Item
from format import BaseFormatter
from receipt import Receipt


class BaseItemFormatter(BaseFormatter):
    """
    Base class for item formatting implementations.
    """

    @abstractmethod
    def format_item(self, item: Item) -> str:
        pass

    def format(self, receipt: Receipt):
        return list(map(self.format_item, receipt.items))


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
