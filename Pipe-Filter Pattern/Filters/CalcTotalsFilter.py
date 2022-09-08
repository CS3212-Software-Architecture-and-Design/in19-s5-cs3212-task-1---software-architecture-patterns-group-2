from Filters.AbstractFilter import AbstractFilter
from Invoice import Invoice

class CalcTotalsFilter(AbstractFilter):
    def process(self, invoice: Invoice) -> Invoice:
        unitPriceLst = invoice.getUnitPrices()
        quantityLst = invoice.getQuantities()
        totalPriceLst = []

        for i in range(len(unitPriceLst)):
            totalPriceLst.append(float(unitPriceLst[i]) * int(quantityLst[i]))
        invoice.getDetailsDict()["TotalPrices"] = totalPriceLst

        print(invoice.getDetailsDict()["TotalPrices"])
        
        return invoice