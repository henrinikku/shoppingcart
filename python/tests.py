import unittest
from typing import List, Tuple

from item import Item
from item_format import PriceFirstItemFormatter, PriceLastItemFormatter
from receipt import Receipt
from receipt_format import ReceiptFormatter
from shopping_cart import ShoppingCartConcreteCreator
from test_utils import Capturing
from total_line_format import ItemCountTotalLineFormatter, PriceOnlyTotalLineFormatter


class ReceiptTest(unittest.TestCase):
    def test_total_price_calculation(self):
        receipt = Receipt(
            [
                Item("banana", 10, 1),
                Item("apple", 10, 12),
                Item("orange", 99, 100),
            ]
        )

        self.assertEqual(receipt.total_price, 10030)

    def test_total_items_calculation(self):
        receipt = Receipt(
            [
                Item("banana", 10, 1),
                Item("apple", 10, 12),
                Item("orange", 99, 100),
            ]
        )

        self.assertEqual(receipt.total_items, 113)


class ItemTest(unittest.TestCase):
    def test_total_price_calculation(self):
        item = Item("foo", 9, 10)
        self.assertEqual(item.total_price, 90)

    def test_total_price_calculation_with_free_price(self):
        item = Item("foo", 0, 10)
        self.assertEqual(item.total_price, 0)


class TotalLineFormatterTest(unittest.TestCase):
    def test_total_line_formatting(self):
        total_line_formatter = PriceOnlyTotalLineFormatter()

        total_line = total_line_formatter.format_total(
            Receipt(
                [
                    Item("first", 100, 1),
                    Item("second", 0, 999),
                    Item("third", 2, 100),
                ]
            )
        )

        self.assertEqual(total_line, "Total price: 300")

    def test_total_line_is_formatted_for_zero_price(self):
        total_line_formatter = PriceOnlyTotalLineFormatter()

        total_line = total_line_formatter.format_total(
            Receipt(
                [
                    Item("first", 100, 0),
                    Item("second", 100, 0),
                    Item("third", 100, 0),
                ]
            )
        )

        self.assertEqual(total_line, "Total price: 0")

    def test_total_line_formatting_with_only_price(self):
        total_line_formatter = PriceOnlyTotalLineFormatter()

        total_line = total_line_formatter.format_total(
            Receipt(
                [
                    Item("banana", 10, 1),
                    Item("apple", 10, 12),
                    Item("orange", 99, 100),
                ]
            )
        )

        self.assertEqual(total_line, "Total price: 10030")

    def test_total_line_formatting_with_item_count(self):
        total_line_formatter = ItemCountTotalLineFormatter()

        total_line = total_line_formatter.format_total(
            Receipt(
                [
                    Item("banana", 10, 1),
                    Item("apple", 10, 12),
                    Item("orange", 99, 100),
                ]
            )
        )

        self.assertEqual(total_line, "Total price (113 items): 10030")


class ItemFormatterTest(unittest.TestCase):
    def test_item_line_formatting_with_price_last(self):
        item_formatter = PriceLastItemFormatter()

        item_line = item_formatter.format_item(Item("banana", 2, 1))
        self.assertEqual(item_line, "banana - 1 - 2")

    def test_item_line_formatting_with_price_first(self):
        item_formatter = PriceFirstItemFormatter()

        item_line = item_formatter.format_item(Item("banana", 2, 1))
        self.assertEqual(item_line, "2 - banana - 1")


class ReceiptFormatterTest(unittest.TestCase):
    def setUp(self):
        self.receipt_formatter = ReceiptFormatter(
            PriceLastItemFormatter(), PriceOnlyTotalLineFormatter()
        )

    def test_receipt_formatting(self):
        receipt = self.receipt_formatter.get_receipt(
            Receipt(
                [
                    Item("banana", 10, 1),
                    Item("apple", 10, 12),
                    Item("orange", 99, 100),
                ]
            )
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


class ShoppingCartTest(unittest.TestCase):
    def setUp(self):
        self.shopping_cart = ShoppingCartConcreteCreator().operation()

    def assert_shopping_cart_output(
        self, items: Tuple[str, int], expected_output: List[str]
    ):
        for name, quantity in items:
            self.shopping_cart.add_item(name, quantity)

        with Capturing() as output:
            self.shopping_cart.print_receipt()

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
