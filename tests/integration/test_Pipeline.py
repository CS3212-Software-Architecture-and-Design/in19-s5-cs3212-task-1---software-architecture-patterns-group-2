import unittest
import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "../../Pipe-Filter Pattern"
abs_file_path = os.path.join(script_dir, rel_path)

import sys

sys.path.append(abs_file_path)

import Invoice
import Pipeline
from Filters import ReadFilter, CalcDiscountsFilter, CalcFinalPriceFilter, CalcTotalsFilter, WriteFilter

class TestPipeline(unittest.TestCase):

    def setUp(self):
        self.filters = []
        self.invoice = Invoice.Invoice("f1.txt")
        self.pipeline = Pipeline.Pipeline()

    def tearDown(self):
        pass

    def test_Read(self):
        
        self.filters = [ReadFilter.ReadFilter()]
        self.add_filters()

        self.pipeline.generateInvoice(self.invoice)

        filter_output = self.invoice.getDetailsDict()
        expected_output = {
            'ItemNames': ['item1', 'item2', 'item3', 'item4'], 
            'UnitPrices': ['100', '190', '30', '1000'], 
            'Quantities': ['3', '2', '4', '1'], 
            'Discounts': ['0', '4', '5', '2']
        }

        self.assertDictEqual(filter_output, expected_output)

    def test_Read_CalcTotals(self):
        
        self.filters = [ReadFilter.ReadFilter(), CalcTotalsFilter.CalcTotalsFilter()]
        self.add_filters()

        self.pipeline.generateInvoice(self.invoice)

        filter_output = self.invoice.getDetailsDict()
        expected_output = {
            'ItemNames': ['item1', 'item2', 'item3', 'item4'], 
            'UnitPrices': ['100', '190', '30', '1000'], 
            'Quantities': ['3', '2', '4', '1'], 
            'Discounts': ['0', '4', '5', '2'], 
            'TotalPrices': [300.0, 380.0, 120.0, 1000.0]
        }

        self.assertDictEqual(filter_output, expected_output)

    def test_Read_CalcTotals_CalcDiscounts(self):
        
        self.filters = [ReadFilter.ReadFilter(), CalcTotalsFilter.CalcTotalsFilter(), CalcDiscountsFilter.CalcDiscountsFilter()]
        self.add_filters()

        self.pipeline.generateInvoice(self.invoice)

        filter_output = self.invoice.getDetailsDict()
        expected_output = {
            'ItemNames': ['item1', 'item2', 'item3', 'item4'], 
            'UnitPrices': ['100', '190', '30', '1000'], 
            'Quantities': ['3', '2', '4', '1'], 
            'Discounts': ['0', '4', '5', '2'], 
            'TotalPrices': [300.0, 380.0, 120.0, 1000.0], 
            'DiscountAmounts': [0.0, 15.2, 6.0, 20.0], 
            'TotalDiscount': 41.2
        }

        self.assertDictEqual(filter_output, expected_output)

    def test_Read_CalcTotals_CalcDiscounts_CalcFinalPrice(self):
        
        self.filters = [ReadFilter.ReadFilter(), CalcTotalsFilter.CalcTotalsFilter(), CalcDiscountsFilter.CalcDiscountsFilter(), CalcFinalPriceFilter.CalcFinalPriceFilter()]
        self.add_filters()

        self.pipeline.generateInvoice(self.invoice)

        filter_output = self.invoice.getDetailsDict()
        expected_output = {
            'ItemNames': ['item1', 'item2', 'item3', 'item4'], 
            'UnitPrices': ['100', '190', '30', '1000'], 
            'Quantities': ['3', '2', '4', '1'], 
            'Discounts': ['0', '4', '5', '2'], 
            'TotalPrices': [300.0, 380.0, 120.0, 1000.0], 
            'DiscountAmounts': [0.0, 15.2, 6.0, 20.0], 
            'TotalDiscount': 41.2, 
            'FinalPrices': [300.0, 364.8, 114.0, 980.0], 
            'FinalTotalPrice': 1758.8
        }

        self.assertDictEqual(filter_output, expected_output)
    
    def test_Read_CalcTotals_CalcDiscounts_CalcFinalPrice_Write(self):
        
        self.filters = [ReadFilter.ReadFilter(), CalcTotalsFilter.CalcTotalsFilter(), CalcDiscountsFilter.CalcDiscountsFilter(), CalcFinalPriceFilter.CalcFinalPriceFilter(), WriteFilter.WriteFilter()]
        self.add_filters()

        self.pipeline.generateInvoice(self.invoice)

        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        rel_path = "../../Pipe-Filter Pattern/TextFiles/Invoice_f1.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        file = open(abs_file_path,"r")

        lst= [line for line in file.read().split("\n")]

        raw_lst = [
            "item1,100,3,0,300.0,0.0,300.0",
            "item2,190,2,4,380.0,15.2,364.8",
            "item3,30,4,5,120.0,6.0,114.0",
            "item4,1000,1,2,1000.0,20.0,980.0",
            "Total discount: 41.2",
            "Total price: 1758.8"
        ]

        self.assertEqual(lst, raw_lst)

    def add_filters(self):

        for filter in self.filters:
            self.pipeline.appendFilter(filter)

if __name__ == '__main__':
    unittest.main()