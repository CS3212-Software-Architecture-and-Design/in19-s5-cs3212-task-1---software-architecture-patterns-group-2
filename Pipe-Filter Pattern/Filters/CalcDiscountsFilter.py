from Filters.AbstractFilter import AbstractFilter
from Invoice import Invoice
import os
class CalcDiscountsFilter(AbstractFilter):
    def process(self, invoice: Invoice) -> Invoice:
        totalPriceList = invoice.getTotalPrices()
        discountList = invoice.getDiscounts()
        discountAmounts = []
        for i in range(len(totalPriceList)):
            discountAmounts.append(float(totalPriceList[i])*float(discountList[i])/100)
        detailsDict = invoice.getDetailsDict()
        detailsDict["DiscountAmounts"] = discountAmounts
        detailsDict["TotalDiscount"] =  sum(discountAmounts)
        #print (invoice.getDetailsDict())
        # print("calcdisc")
        # print(invoice.getDetailsDict())
        # print()
                
        return invoice
