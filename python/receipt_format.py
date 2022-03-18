import itertools
from abc import ABC, abstractmethod
from typing import Tuple
from receipt import Receipt
from format import BaseFormatter
from item_format import PriceLastItemFormatter
from total_line_format import PriceOnlyTotalLineFormatter


class ReceiptFormatter:
    """
    Implements receipt formatting.
    """

    def __init__(self, formatters: Tuple[BaseFormatter, ...]):
        self.formatters = formatters

    def get_receipt(self, receipt: Receipt):
        """
        Turns given receipt into a formatted string using formatters given to the class.
        """
        receipt_lines = itertools.chain(
            *[formatter.format(receipt) for formatter in self.formatters]
        )
        return "\n".join(receipt_lines)


class ReceiptFormatterCreator(ABC):
    """
    Interface for the ReceiptFormatterCreator creator.
    """

    @abstractmethod
    def factory_method(self) -> ReceiptFormatter:
        pass

    def operation(self) -> ReceiptFormatter:
        return self.factory_method()


class ReceiptFormatterConcreteCreator(ReceiptFormatterCreator):
    def factory_method(self) -> ReceiptFormatter:
        return ReceiptFormatter(
            formatters=(
                PriceLastItemFormatter(),
                PriceOnlyTotalLineFormatter(),
            )
        )
