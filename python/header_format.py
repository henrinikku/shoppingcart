from format import BaseFormatter
from receipt import Receipt


class HeaderFormatter(BaseFormatter):
    """
    Renders header text.
    """
    def __init__(self, header_text: str):
        self.header_text = header_text

    def format(self, receipt: Receipt):
        return [self.header_text]
