from receipt import Receipt
from item_format import BaseItemFormatter


class ReceiptFormatter:
    def __init__(self, item_formatter: BaseItemFormatter):
        self.item_formatter = item_formatter

    def format_total(self, receipt: Receipt):
        return f"Total price: {receipt.total_price}"

    def get_receipt(self, receipt: Receipt):
        item_lines = map(self.item_formatter.format_item, receipt.items)
        total_line = self.format_total(receipt)
        return "\n".join(list(item_lines) + [total_line])
