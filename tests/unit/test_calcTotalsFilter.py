import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "../../Pipe-Filter Pattern"
abs_file_path = os.path.join(script_dir, rel_path)

import sys

sys.path.append(abs_file_path)

import unittest
from Filters.CalcTotalsFilter import CalcTotalsFilter
from Invoice import Invoice

class TestCalcTotalsFilter(unittest.TestCase):
    def test_calc_total_process(self):
        invoice = Invoice("")
        invoice.setUnitPrices(['100', '190', '30', '1000'])
        invoice.setQuantites(['3', '2', '4', '1'])

        CalcTotalsFilter().process(invoice)

        self.assertEqual(invoice.getTotalPrices(), [300.0, 380.0, 120.0, 1000.0])
       
if __name__ == "__main__":
    unittest.main()