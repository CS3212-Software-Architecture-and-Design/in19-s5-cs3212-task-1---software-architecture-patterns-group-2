import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "../../Pipe-Filter Pattern"
abs_file_path = os.path.join(script_dir, rel_path)

import sys

sys.path.append(abs_file_path)

import unittest
from Filters.CalcDiscountsFilter import CalcDiscountsFilter
from Invoice import Invoice

class TestCalcDiscounts(unittest.TestCase):
    def test_process(self):
        invoice = Invoice('f1.txt')
        invoice.getDetailsDict()['TotalPrices'] = [300.0, 380.0, 120.0, 1000.0]
        invoice.getDetailsDict()['Discounts'] = ['0', '4', '5', '2']
        CalcDiscountsFilter().process(invoice)
        self.assertEqual(invoice.getDiscountAmounts(), [0.0, 15.2, 6.0, 20.0])

if __name__ == '__main__':
    unittest.main()