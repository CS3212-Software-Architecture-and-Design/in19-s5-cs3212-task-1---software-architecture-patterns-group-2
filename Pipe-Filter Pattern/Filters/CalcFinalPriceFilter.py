from Filters.AbstractFilter import AbstractFilter
from Invoice import Invoice


class CalcFinalPriceFilter(AbstractFilter):
    def process(self, invoice: Invoice) -> Invoice:
        # get the list with the unit_price*quantity values for each item
        totalPrices = invoice.getTotalPrices(invoice)
        # get list with the discounted amounts for each item
        discountAmounts = invoice.getDiscountAmounts(invoice)
        finalPrices = []
        for i in range(len(totalPrices)):
            # final price of the item = total price of the item - discount amount of the item
            finalPrices.append((totalPrices[i])-discountAmounts[i])
            invoice.getDetailsDict()["FinalPrices"] = finalPrices
            invoice.getDetailsDict()["FinalTotalPrice"] = sum(
                finalPrices)  # get the sum of final prices of the items

        return invoice
