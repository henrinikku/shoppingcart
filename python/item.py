from dataclasses import dataclass


@dataclass
class Item:
    name: str
    price: int
    count: int = 0

    @property
    def total_price(self):
        return self.price * self.count
