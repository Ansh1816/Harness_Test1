import unittest
from pocketledger.money import to_cents
from pocketledger.reader import read_expenses
from pocketledger.filters import select
from pocketledger.report import summarize

def rows():
    return read_expenses("date,category,amount,note\n2026-09-01,Travel,10.00,Bus\n2026-09-30,Travel,-2.00,Refund\n")

class LedgerTests(unittest.TestCase):
    def test_fractional_cent_rounds_half_up(self):
        self.assertEqual(to_cents("1.005"), 101)
    def test_csv_quoted_note(self):
        data = 'date,category,amount,note\n2026-09-01,Food,3.50,"Lunch, coffee"\n'
        self.assertEqual(read_expenses(data)[0].note, "Lunch, coffee")
    def test_end_date_inclusive(self):
        self.assertEqual(len(select(rows(), end="2026-09-30")), 2)
    def test_category_query_case_insensitive(self):
        self.assertEqual(len(select(rows(), category=" TRAVEL ")), 2)
    def test_credits_reduce_total(self):
        self.assertEqual(summarize(rows())["total_cents"], 800)
    def test_whole_amount(self):
        self.assertEqual(to_cents("12.50"), 1250)
    def test_negative_amount(self):
        self.assertEqual(to_cents("-2.00"), -200)
    def test_nonfinite_rejected(self):
        with self.assertRaises(ValueError):
            to_cents("NaN")
    def test_invalid_date_rejected(self):
        with self.assertRaises(ValueError):
            read_expenses("date,category,amount,note\n2026-02-30,food,1,x\n")
    def test_empty_category_rejected(self):
        with self.assertRaises(ValueError):
            read_expenses("date,category,amount,note\n2026-09-01, ,1,x\n")
    def test_start_inclusive(self):
        self.assertEqual(len(select(rows(), start="2026-09-01")), 2)
    def test_reverse_range_rejected(self):
        with self.assertRaises(ValueError):
            select(rows(), start="2026-09-30", end="2026-09-01")
    def test_missing_category(self):
        self.assertEqual(select(rows(), category="books"), [])
    def test_empty_report(self):
        self.assertEqual(summarize([]), {"count": 0, "total_cents": 0, "by_category": {}})
    def test_category_net_total(self):
        self.assertEqual(summarize(rows())["by_category"], {"travel": 800})
