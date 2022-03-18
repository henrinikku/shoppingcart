from abc import ABC, abstractmethod
from receipt import Receipt


class BaseTotalLineFormatter(ABC):
    @abstractmethod
    def format_total(self, receipt: Receipt):
        pass


class PriceOnlyTotalLineFormatter(BaseTotalLineFormatter):
    def format_total(self, receipt: Receipt):
        return f"Total price: {receipt.total_price}"


class ItemCountTotalLineFormatter(BaseTotalLineFormatter):
    def format_total(self, receipt: Receipt):
        return f"Total price ({receipt.total_items} items): {receipt.total_price}"
