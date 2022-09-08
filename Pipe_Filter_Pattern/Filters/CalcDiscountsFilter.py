from Filters.AbstractFilter import AbstractFilter
from Invoice import Invoice
import os
class CalcDiscountsFilter(AbstractFilter):
    def process(self, invoice: Invoice) -> Invoice:
        # totalPriceList = ['300', '380', '120', '1000']
        totalPriceList = invoice.getTotalPrices()
        discountList = invoice.getDiscounts()
        discountAmounts = []
        for i in range(len(totalPriceList)):
            discountAmounts.append(float(totalPriceList[i])*float(discountList[i])/100)
        detailsDict = invoice.getDetailsDict()
        detailsDict["DiscountAmounts"] = discountAmounts
        detailsDict["TotalDiscount"] =  sum(discountAmounts)
        print (detailsDict)
                
        return invoice
