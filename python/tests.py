import unittest

from shopping_cart import ShoppingCartConcreteCreator
from receipt import ReceiptFormatter, ReceiptItem, ReceiptItemFormat
from test_utils import Capturing


class ReceiptFormatterTest(unittest.TestCase):
    def setUp(self):
        self.receipt_formatter = ReceiptFormatter()

    def test_get_normal_receipt(self):
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
    def test_print_receipt(self):
        sc = ShoppingCartConcreteCreator().operation()
        sc.add_item("apple", 2)

        with Capturing() as output:
            sc.print_receipt()

        self.assertEqual(
            output,
            [
                "apple - 2 - 100",
                "Total price: 200",
            ],
        )

    def test_items_are_printed_in_the_order_they_were_added(self):
        sc = ShoppingCartConcreteCreator().operation()
        sc.add_item("banana", 5)
        sc.add_item("apple", 2)
        sc.add_item("third", 2)
        sc.add_item("fourth", 2)
        sc.add_item("fifth", 2)

        with Capturing() as output:
            sc.print_receipt()

        self.assertEqual(
            output,
            [
                "banana - 5 - 200",
                "apple - 2 - 100",
                "third - 2 - 0",
                "fourth - 2 - 0",
                "fifth - 2 - 0",
                "Total price: 1200",
            ],
        )

    def test_doesnt_explode_on_mystery_item(self):
        sc = ShoppingCartConcreteCreator().operation()
        sc.add_item("apple", 2)
        sc.add_item("banana", 5)
        sc.add_item("pear", 5)
        with Capturing() as output:
            sc.print_receipt()
        self.assertEqual("apple - 2 - 100", output[0])
        self.assertEqual("banana - 5 - 200", output[1])
        self.assertEqual("pear - 5 - 0", output[2])


unittest.main(exit=False)
