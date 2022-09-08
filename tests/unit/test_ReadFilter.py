import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "../../Pipe-Filter Pattern"
abs_file_path = os.path.join(script_dir, rel_path)

import sys

sys.path.append(abs_file_path)

import unittest
from Filters.ReadFilter import ReadFilter
from Invoice import Invoice


class TestReadFilter(unittest.TestCase):

    def test_read_filter(self):

        invoiceObj2 = ReadFilter().process(Invoice("f1.txt"))
        invoiceObj1 = Invoice("f1.txt")
        invoiceObj1.setDetailsDict({
            'ItemNames': ['item1', 'item2', 'item3', 'item4'], 
            'UnitPrices': ['100', '190', '30', '1000'], 
            'Quantities': ['3', '2', '4', '1'], 
            'Discounts': ['0', '4', '5', '2']
        })
        self.assertDictEqual(invoiceObj1.getDetailsDict(), invoiceObj2.getDetailsDict())


if __name__ == '__main__':
    unittest.main()