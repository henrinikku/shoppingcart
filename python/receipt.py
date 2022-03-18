from enum import Enum, auto
from typing import List

from item import Item
from item_format import BaseItemFormatter


class ReceiptFormatter:
    def __init__(self, item_formatter: BaseItemFormatter):
        self.item_formatter = item_formatter

    def format_total(self, items: List[Item]):
        total = sum(item.total_price for item in items)
        return f"Total price: {total}"

    def get_receipt(self, items: List[Item]):
        item_lines = map(self.item_formatter.format_item, items)
        total_line = self.format_total(items)
        return "\n".join(list(item_lines) + [total_line])
