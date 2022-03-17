from abc import ABC, abstractmethod
from collections import defaultdict
from typing import Dict
from receipt import ReceiptFormatter, ReceiptItem

from shopping_cart_interface import IShoppingCart
from pricer import Pricer

class ShoppingCart(IShoppingCart):
    """
    Implementation of the shopping tills in our supermarket.
    """
    def __init__(self, pricer: Pricer, receipt_formatter: ReceiptFormatter):
        self.pricer = pricer
        self.receipt_formatter = receipt_formatter
        self._contents: Dict[str,int] = defaultdict(int)

    def add_item(self, item_type: str, number: int):
        # adds new item to or update existing item in the shopping cart
        self._contents[item_type] += number

    def get_receipt_items(self):
        for item_name, item_count in self._contents.items():
            price = self.pricer.get_price(item_name)
            yield ReceiptItem(item_name, item_count, price)

    def print_receipt(self):
        receipt_items = list(self.get_receipt_items())
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
        return ShoppingCart(Pricer(), ReceiptFormatter())
