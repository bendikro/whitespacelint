from __future__ import print_function

import testtools

from whitespacelint import whitespacelint


class TestCheckers(testtools.TestCase):

    def _check_ok(self, checker, cases, **args):
        for case in cases:
            self.assertIsNone(checker(case, **args))

    def _check_error(self, checker, cases, **args):
        for case, offset in cases:
            result = checker(case, **args)
            self.assertIsNotNone(result)
            self.assertEqual(result[0], offset, "\nTestcase: '%s'\n" % case)

    def test_w201_ok(self):
        self._check_ok(whitespacelint.checker_trailing_whitespace, [
            "\n",
            "\r",
            "echo Test",
            "echo Test\n",
            "echo Test\r",
        ])

    def test_w201_error(self):
        self._check_error(whitespacelint.checker_trailing_whitespace, [
            ("\n ", 1),
            (" \n", 0),
            ("echo Test ", 9),
            ("echo Test\n ", 10),
            ("echo Test \n", 9),
            ("echo Test \n ", 11),
        ])

    def test_w202_ok(self):
        self._check_ok(whitespacelint.checker_trailing_whitespace, [
            "",
        ])

    def test_w202_error(self):
        self._check_error(whitespacelint.checker_trailing_whitespace, [
            (" ", 0),
            ("    ", 0),
        ])

    def test_w203_ok(self):
        self._check_ok(whitespacelint.checker_trailing_semicolon, [
            "",
            "echo Test",
            "echo Test; echo Test2",
            " ;; ",
            "find -type f -exec cat {} \;",
        ])

    def test_w203_error(self):
        self._check_error(whitespacelint.checker_trailing_semicolon, [
            (";", 0),
            ("    ;", 4),
            ("echo Test;", 9),
            ("echo Test;  ", 9),
            ("echo Test; echo Test2;", 21),
        ])

    def test_w204_ok(self):
        self._check_ok(whitespacelint.checker_no_newline_on_last_line, [
            "",
        ], last_line=False)
        self._check_ok(whitespacelint.checker_no_newline_on_last_line, [
            "\n",
        ], last_line=True)

    def test_w204_error(self):
        self._check_error(whitespacelint.checker_no_newline_on_last_line, [
            ("", 0),
        ], last_line=True)

    def test_w205_ok(self):
        self._check_ok(whitespacelint.checker_multiple_newlines_at_end_of_file, [
            "",
        ], last_line=False)
        self._check_ok(whitespacelint.checker_multiple_newlines_at_end_of_file, [
            "test\n",
        ], last_line=True)

    def test_w205_error(self):
        self._check_error(whitespacelint.checker_multiple_newlines_at_end_of_file, [
            ("", 0),
        ], last_line=True)
        self._check_error(whitespacelint.checker_multiple_newlines_at_end_of_file, [
            ("\n", 0),
        ], last_line=True)
