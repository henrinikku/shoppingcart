# Notes

## TODO

- [x] Add a 'Total' line to the receipt. This should be the full price we should charge the customer.
- [x] Make the receipt print items in the order that they were scanned.
- [x] In some branches of the store, customers want the receipt to show the price first on each line. Without changing the IShoppingCart interface, add a way to support this which allows for other formatting options in the future.
- [x] One limitation of the codebase is that every time a change is made, many of the tests need updating. Update or replace the test suite to extend coverage and limit the number of tests which need updating when changes are introduced.
- [ ] Improve the solution & tests. There are no rules/limitations other than conforming to the IShoppingCart interface - go crazy.

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

## Ideas

- Use some inheritance-based pattern (e.g. mixins) for specifying receipt formatting rules instead of enums.
- Make `Pricer` more extensible -- get rid of hard coded items etc.
- Create a class to represent items in a shopping cart that could be used by `ShoppingCart` and `ReceiptFormatter` classes.
- Add more test cases.
