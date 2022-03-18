from dataclasses import dataclass


@dataclass
class Item:
    """
    Represents a single item in shopping cart or receipt.
    """

    name: str
    price: int
    count: int = 0

    @property
    def total_price(self):
        """
        Calculates the total price for this item.
        """
        return self.price * self.count
