from Filters.AbstractFilter import AbstractFilter
from Invoice import Invoice

class CalcTotalsFilter(AbstractFilter):
    def process(self, invoice: Invoice) -> Invoice:
        unitPriceLst = invoice.getUnitPrices()    # get the unit price list of items
        quantityLst = invoice.getQuantities()  # get the quantity list of items
        totalPriceLst = []

        for i in range(len(unitPriceLst)):
            totalPriceLst.append(float(unitPriceLst[i]) * int(quantityLst[i]))  # calculate the total price for each item
        invoice.setTotalPrices(totalPriceLst)  # set the total price list for items        
        return invoice