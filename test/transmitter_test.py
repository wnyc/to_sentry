from to_sentry.transmitter import format_text
import unittest

class TestTransmitter(unittest.TestCase):
    def test_format_text(self):
        self.assertEquals(list(format_text("stdin", "1\n2\n3")),
                               [("stdin.00000000","1"),
                                ("stdin.00000001", "2"),
                                ("stdin.00000002", "3")])
    def test_format_skips_blank_linestext(self):
        self.assertEquals(list(format_text("stdin", "1\n2\n\n3")),
                               [("stdin.00000000","1"),
                                ("stdin.00000001", "2"),
                                ("stdin.00000003", "3")])
