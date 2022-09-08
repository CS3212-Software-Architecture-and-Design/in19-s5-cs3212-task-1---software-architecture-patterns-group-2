import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "../../Pipe-Filter Pattern"
abs_file_path = os.path.join(script_dir, rel_path)

import sys

sys.path.append(abs_file_path)

import unittest
from Filters.CalcFinalPriceFilter import CalcFinalPriceFilter
from Invoice import Invoice


class TestCalcFinalPriceFilter(unittest.TestCase):
    def test_process(self):
        invoice = Invoice("")
        invoice.getDetailsDict()["TotalPrices"] = [
            300.0, 380.0, 120.0, 1000]
        invoice.getDetailsDict()["DiscountAmounts"] = [0.0, 15.2, 6.0, 20.0]
        CalcFinalPriceFilter().process(invoice)
        finalPrices = invoice.getFinalPrices()
        finalTotalPrice = invoice.getFinalTotalPrice()
        self.assertEqual(finalPrices, [300.0, 364.8, 114.0, 980.0])
        self.assertEqual(finalTotalPrice, 1758.8)


if __name__ == '__main__':
    unittest.main()
