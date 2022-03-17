from dataclasses import dataclass
from enum import Enum, auto
from typing import List


class ReceiptItemFormat(Enum):
    price_last = auto()
    price_first = auto()


@dataclass
class ReceiptItem:
    name: str
    count: int
    price: int


class ReceiptFormatter:
    def __init__(
        self, receipt_item_format: ReceiptItemFormat = ReceiptItemFormat.price_last
    ):
        self.receipt_item_format = receipt_item_format

    def format_item(self, item: ReceiptItem):
        if self.receipt_item_format == ReceiptItemFormat.price_first:
            return f"{item.price} - {item.name} - {item.count}"

        return f"{item.name} - {item.count} - {item.price}"

    def format_total(self, items: List[ReceiptItem]):
        total = sum(item.price * item.count for item in items)
        return f"Total price: {total}"

    def get_receipt(self, items: List[ReceiptItem]):
        item_lines = [self.format_item(item) for item in items]
        total_line = self.format_total(items)
        return "\n".join(item_lines + [total_line])
