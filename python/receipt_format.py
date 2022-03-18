from receipt import Receipt
from item_format import BaseItemFormatter
from total_line_format import BaseTotalLineFormatter


class ReceiptFormatter:
    def __init__(
        self,
        item_formatter: BaseItemFormatter,
        total_line_formatter: BaseTotalLineFormatter,
    ):
        self.item_formatter = item_formatter
        self.total_line_formatter = total_line_formatter

    def get_receipt(self, receipt: Receipt):
        item_lines = map(self.item_formatter.format_item, receipt.items)
        total_line = self.total_line_formatter.format_total(receipt)
        return "\n".join(list(item_lines) + [total_line])
