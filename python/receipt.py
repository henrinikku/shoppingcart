from dataclasses import dataclass
from typing import List
from item import Item


@dataclass
class Receipt:
    items: List[Item]

    @property
    def total_price(self):
        return sum(item.total_price for item in self.items)

    @property
    def total_items(self):
        return sum(item.count for item in self.items)
