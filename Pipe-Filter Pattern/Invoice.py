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
            return self.__details["DiscountAmounts"]

    def getTotalPrices(self):
        if "TotalPrices" in self.__details.keys():
            return self.__details["TotalPrices"]

    def getTotalDiscount(self):
        if "TotalDiscount" in self.__details.keys():
            return self.__details["TotalDiscount"]

    def getFinalPrice(self):
        if "FinalPrice" in self.__details.keys():
            return self.__details["FinalPrice"]

    def getFileName(self):
        return self.__file

    def getDetailsDict(self):
        return self.__details
        
    



