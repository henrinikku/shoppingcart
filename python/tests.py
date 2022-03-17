from typing import List, Tuple
import unittest

from shopping_cart import ShoppingCartConcreteCreator
from receipt import ReceiptFormatter, ReceiptItem, ReceiptItemFormat
from test_utils import Capturing


class ReceiptFormatterTest(unittest.TestCase):
    def setUp(self):
        self.receipt_formatter = ReceiptFormatter()

    def test_receipt_formatting(self):
        receipt = self.receipt_formatter.get_receipt(
            [
                ReceiptItem("banana", 1, 10),
                ReceiptItem("apple", 12, 10),
                ReceiptItem("orange", 100, 99),
            ]
        )

        self.assertEqual(
            receipt,
            "\n".join(
                [
                    "banana - 1 - 10",
                    "apple - 12 - 10",
                    "orange - 100 - 99",
                    "Total price: 10030",
                ]
            ),
        )

    def test_total_price_calculation(self):
        total_line = self.receipt_formatter.format_total(
            [
                ReceiptItem("first", 1, 100),
                ReceiptItem("second", 999, 0),
                ReceiptItem("third", 100, 2),
            ]
        )

        self.assertEqual(total_line, "Total price: 300")

    def test_item_line_formatting_with_price_last(self):
        item_line = self.receipt_formatter.format_item(ReceiptItem("banana", 1, 2))
        self.assertEqual(item_line, "banana - 1 - 2")

    def test_item_line_formatting_with_price_first(self):
        self.receipt_formatter.receipt_item_format = ReceiptItemFormat.price_first

        item_line = self.receipt_formatter.format_item(ReceiptItem("banana", 1, 2))
        self.assertEqual(item_line, "2 - banana - 1")


class ShoppingCartTest(unittest.TestCase):
    def setUp(self):
        self.sc = ShoppingCartConcreteCreator().operation()

    def assert_shopping_cart_output(
        self, items: Tuple[str, int], expected_output: List[str]
    ):
        for name, quantity in items:
            self.sc.add_item(name, quantity)

        with Capturing() as output:
            self.sc.print_receipt()

        self.assertEqual(output, expected_output)

    def test_print_receipt(self):
        self.assert_shopping_cart_output(
            items=[("apple", 2)],
            expected_output=[
                "apple - 2 - 100",
                "Total price: 200",
            ],
        )

    def test_items_are_printed_in_the_order_they_were_added(self):
        self.assert_shopping_cart_output(
            items=[
                ("banana", 5),
                ("apple", 2),
                ("third", 2),
                ("fourth", 2),
                ("fifth", 2),
            ],
            expected_output=[
                "banana - 5 - 200",
                "apple - 2 - 100",
                "third - 2 - 0",
                "fourth - 2 - 0",
                "fifth - 2 - 0",
                "Total price: 1200",
            ],
        )

    def test_doesnt_explode_on_mystery_item(self):
        self.assert_shopping_cart_output(
            items=[("apple", 2), ("banana", 5), ("pear", 5)],
            expected_output=[
                "apple - 2 - 100",
                "banana - 5 - 200",
                "pear - 5 - 0",
                "Total price: 1200",
            ],
        )


unittest.main(exit=False)
