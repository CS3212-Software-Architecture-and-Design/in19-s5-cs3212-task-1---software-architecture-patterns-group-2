class Invoice:

    __file = None
    __details = None
    def __init__(self, txtFile) -> None:
        self.__file = txtFile
        self.__details={}

    def getItemNames(self):
        if "ItemNames" in self.__details.keys():
            return self.__details["ItemNames"]

    def getQuantities(self):
        if "Quantities" in self.__details.keys():
            return self.__details["Quantities"]

    def getUnitPrices(self):
        if "UnitPrices" in self.__details.keys():
            return self.__details["UnitPrices"]

    def getDiscounts(self):
        if "Discounts" in self.__details.keys():
            return self.__details["Discounts"]

    def getDiscountAmounts(self):
        if "DiscountAmounts" in self.__details.keys():
            return self.__details["DiscountAmounts"] #a list with the discounted amounts for each item

    def getTotalPrices(self):
        if "TotalPrices" in self.__details.keys():
            return self.__details["TotalPrices"] #a list with the unit_price*quantity values for each item

    def getFinalPrices(self):
        if "FinalPrices" in self.__details.keys():
            return self.__details["FinalPrices"] #a list with the final prices(including discounts) for each item
    
    def getFinalTotalPrice(self):
        if "FinalTotalPrice" in self.__details.keys():
            return self.__details["FinalTotalPrice"] # Overall total price to be paid

    def getTotalDiscount(self):
        if "TotalDiscount" in self.__details.keys():
            return self.__details["TotalDiscount"] # total discount 

    def getFileName(self):
        return self.__file

    def getDetailsDict(self):
        return self.__details

    def setDetailsDict(self, dict):
        self.__details = dict

    def setQuantites(self, lst):
        self.__details["Quantities"] = lst

    def setUnitPrices(self, lst):
        self.__details["UnitPrices"] = lst
        
    def setTotalPrices(self, lst):
        self.__details["TotalPrices"] = lst
    



