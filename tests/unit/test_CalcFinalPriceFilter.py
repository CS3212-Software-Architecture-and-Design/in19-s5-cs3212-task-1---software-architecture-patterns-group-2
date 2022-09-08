import unittest
from Filters.CalcFinalPriceFilter import CalcFinalPriceFilter
from Invoice import Invoice


class TestCalcFinalPriceFilter(unittest.TestCase):
    def test_process(self):
        invoiceObj = Invoice('f1.txt')
        invoiceObj.getDetailsDict()["TotalPrices"] = [
            300.0, 380.0, 120.0, 1000]
        invoiceObj.getDetailsDict()["DiscountAmounts"] = [0.0, 15.2, 6.0, 20.0]
        invoiceObj = CalcFinalPriceFilter.process(invoiceObj)
        finalPrices = invoiceObj.getFinalPrices()
        finalTotalPrice = invoiceObj.getFinalTotalPrice()
        self.assertEqual(finalPrices, [300.0, 364.8, 114.0, 980.0])
        self.assertEqual(finalTotalPrice, 1758.8)


if __name__ == '__main__':
    unittest.main()
