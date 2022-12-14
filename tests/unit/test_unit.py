import os
import sys
import unittest

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "../../Pipe-Filter Pattern"
abs_file_path = os.path.join(script_dir, rel_path)
sys.path.append(abs_file_path)

from Filters import ReadFilter, CalcTotalsFilter, CalcDiscountsFilter, CalcFinalPriceFilter, WriteFilter
from Invoice import Invoice

class TestFilters(unittest.TestCase):
    def test_read_process(self):
        invoiceObj2 = ReadFilter.ReadFilter().process(Invoice("f1.txt"))
        invoiceObj1 = Invoice("f1.txt")
        invoiceObj1.setDetailsDict({
            'ItemNames': ['item1', 'item2', 'item3', 'item4'], 
            'UnitPrices': ['100', '190', '30', '1000'], 
            'Quantities': ['3', '2', '4', '1'], 
            'Discounts': ['0', '4', '5', '2']
        })
        self.assertDictEqual(invoiceObj1.getDetailsDict(), invoiceObj2.getDetailsDict())

    def test_calc_total_process(self):
        invoice = Invoice("")
        invoice.setUnitPrices(['100', '190', '30', '1000'])
        invoice.setQuantites(['3', '2', '4', '1'])

        CalcTotalsFilter.CalcTotalsFilter().process(invoice)

        self.assertEqual(invoice.getTotalPrices(), [300.0, 380.0, 120.0, 1000.0])

    def test_clac_discount_process(self):
        invoice = Invoice('f1.txt')
        invoice.getDetailsDict()['TotalPrices'] = [300.0, 380.0, 120.0, 1000.0]
        invoice.getDetailsDict()['Discounts'] = ['0', '4', '5', '2']
        CalcDiscountsFilter.CalcDiscountsFilter().process(invoice)
        self.assertEqual(invoice.getDiscountAmounts(), [0.0, 15.2, 6.0, 20.0])

    def test_calc_final_price_process(self):
        invoice = Invoice("")
        invoice.getDetailsDict()["TotalPrices"] = [
            300.0, 380.0, 120.0, 1000]
        invoice.getDetailsDict()["DiscountAmounts"] = [0.0, 15.2, 6.0, 20.0]
        CalcFinalPriceFilter.CalcFinalPriceFilter().process(invoice)
        finalPrices = invoice.getFinalPrices()
        finalTotalPrice = invoice.getFinalTotalPrice()
        self.assertEqual(finalPrices, [300.0, 364.8, 114.0, 980.0])
        self.assertEqual(finalTotalPrice, 1758.8)

    def test_write_process(self):
        test_dict = {
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
        invoice = Invoice("f1.txt")
        invoice.setDetailsDict(test_dict)

        writeFilter = WriteFilter.WriteFilter()
        writeFilter.process(invoice)

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

if __name__ == '__main__':
    unittest.main()

