from Invoice import Invoice 
from Filters import AbstractFilter
class Pipeline:

    __filters =[]
    def __init__(self, filterList =[]) -> None:
        self.__filters = filterList

    def generateInvoice(self, invoiceObj:Invoice):
        for filter in self.__filters:
            invoiceObj = filter.process(invoiceObj)
            if invoiceObj.getError()==1:
                break
        if invoiceObj.getError()==1:
            print("Programme Terminated!")
        else:
            print("Invoice is Generated")

    def appendFilter(self, filter:AbstractFilter):
        self.__filters.append(filter)
    
    def insertFilter(self, filter:AbstractFilter, index):
        self.__filters.insert(index, filter)

    def removeFilter(self, filter):
        self.__filters.remove(filter)

    def getFilters(self)-> list:
        return [filter.name for filter in self.__filters]
