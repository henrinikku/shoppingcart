from abc import ABC, abstractmethod
from receipt import Receipt


class BaseTotalLineFormatter(ABC):
    """
    Base class for total line formatting implementations.
    """

    @abstractmethod
    def format_total(self, receipt: Receipt):
        pass


class PriceOnlyTotalLineFormatter(BaseTotalLineFormatter):
    """
    Total line formatting implementation that shows the total price and nothing else.
    """

    def format_total(self, receipt: Receipt):
        return f"Total price: {receipt.total_price}"


class ItemCountTotalLineFormatter(BaseTotalLineFormatter):
    """
    Total line formatting implementation that shows
    the total price and the total number of items.
    """

    def format_total(self, receipt: Receipt):
        return f"Total price ({receipt.total_items} items): {receipt.total_price}"
