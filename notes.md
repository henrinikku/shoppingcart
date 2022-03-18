# Notes

## TODO

- [x] Add a 'Total' line to the receipt. This should be the full price we should charge the customer.
- [x] Make the receipt print items in the order that they were scanned.
- [x] In some branches of the store, customers want the receipt to show the price first on each line. Without changing the IShoppingCart interface, add a way to support this which allows for other formatting options in the future.
- [x] One limitation of the codebase is that every time a change is made, many of the tests need updating. Update or replace the test suite to extend coverage and limit the number of tests which need updating when changes are introduced.
- [ ] Improve the solution & tests. There are no rules/limitations other than conforming to the IShoppingCart interface - go crazy.
  - [x] Use some inheritance-based pattern for specifying receipt formatting rules instead of enums.
  - [x] Create a class to represent items in a shopping cart that could be used by `ShoppingCart` and `ReceiptFormatter` classes.
  - [x] Create a class to represent a receipt that could be constructed by the `ShoppingCart` class and passed on to, for example, the `ReceiptFormatter` class.
  - [x] Allow speficying different formatting rules for the 'Total' line as well.
  - [x] Add more test cases.
  - [x] Add comments/docstrings for classes.
  - [x] Make it easier to form and combine receipt formatting configurations by refactoring formatter classes such that they all share the same base class and `format` function signature.
  - [ ] Split modules into different folders
  - [ ] Add support for localization (i.e., different currencies etc).
  - [ ] Make `Pricer` more extensible -- get rid of hard coded items etc.

## Sessions

- **Wed 16. March (20 min)**
  - Read through the problem description and source code
  - Added 'Total' line to the receipt
  - Added a test case to ensure items are printed in the order that they were scanned.
- **Thu 17. March (45 min)**
  - Added the `ReceiptFormatter` class and an enum based implementation for specifying receipt formatting rules
  - Added new test cases
  - Reduced the amount boilerplate in `ShoppingCart` test cases
  - Minor readability improvements to `ShoppingCart` class
  - Started using `black` for formatting
- **Fri 18. March (1h 30min)**
  - Added an `Item` class to represent items.
  - Added `ItemFormatter` classes to replace the enum based implementation for specifying receipt item formatting rules.
  - Added test cases.
  - Added an option to specify different formatting rules for the 'Total' line as well.
  - Added the `Receipt` class to represent receipts.
  - Added comments for each class.
- **Fri 18. March (25min)**
  - Refactored `Formatter` classes such that they now share the same base class and can be freely combined in `ReceiptFormatter`.
  - Added `HeaderFormatter` as an example to showcase how formatters can now be more easily combined. See [this test case](https://github.com/henrinikku/shoppingcart/blob/4acbc2b41146a83f97efe1b621452dc5876ca2df/python/tests.py#L186) for example usage.
