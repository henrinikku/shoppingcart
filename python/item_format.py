from abc import ABC, abstractmethod
from item import Item

class BaseItemFormatter(ABC):
    @abstractmethod
    def format_item(self, item: Item):
        pass


class PriceFirstItemFormatter(BaseItemFormatter):
    def format_item(self, item: Item):
        return f"{item.price} - {item.name} - {item.count}"


class PriceLastItemFormatter(BaseItemFormatter):
    def format_item(self, item: Item):
        return f"{item.name} - {item.count} - {item.price}"