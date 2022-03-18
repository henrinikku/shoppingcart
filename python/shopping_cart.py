from abc import ABC, abstractmethod
from collections import defaultdict
from typing import Dict

from item import Item
from item_format import PriceLastItemFormatter
from pricer import Pricer
from receipt_format import ReceiptFormatter
from shopping_cart_interface import IShoppingCart


class ShoppingCart(IShoppingCart):
    """
    Implementation of the shopping tills in our supermarket.
    """

    def __init__(self, pricer: Pricer, receipt_formatter: ReceiptFormatter):
        self.pricer = pricer
        self.receipt_formatter = receipt_formatter
        self._contents: Dict[str, Item] = {}

    def add_item(self, item_type: str, number: int):
        # adds new item to or update existing item in the shopping cart
        if item_type not in self._contents:
            price = self.pricer.get_price(item_type)
            self._contents[item_type] = Item(item_type, price)

        self._contents[item_type].count += number

    def print_receipt(self):
        receipt_items = list(self._contents.values())
        receipt = self.receipt_formatter.get_receipt(receipt_items)
        print(receipt)


class ShoppingCartCreator(ABC):
    """
    Interface for the ShoppingCart creator.
    The creation process will be delegated to the subclasses of this class.
    """

    @abstractmethod
    def factory_method(self) -> ShoppingCart:
        # return the ShoppingCart object
        pass

    def operation(self) -> ShoppingCart:
        # Here more operations can be performed on the ShoppingCart object
        # returns ShoppingCart object
        return self.factory_method()


class ShoppingCartConcreteCreator(ShoppingCartCreator):
    """
    Concrete class for the ShoppingCart creator.
    Implements the factory_method
    """

    def factory_method(self) -> ShoppingCart:
        item_formatter = PriceLastItemFormatter()
        return ShoppingCart(Pricer(), ReceiptFormatter(item_formatter))
