from Filters.AbstractFilter import AbstractFilter
from Invoice import Invoice
import os
class ReadFilter(AbstractFilter):
    def process(self, invoice: Invoice) -> Invoice:
        #print(invoice.getFileName())
        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        rel_path = "../TextFiles/"+invoice.getFileName()
        abs_file_path = os.path.join(script_dir, rel_path)
        file = open(abs_file_path,"r")
        lst= [line.split(",") for line in file.read().split("\n")]
        keysList = ["ItemNames", "UnitPrices","Quantities","Discounts"]
        for i in range(len(keysList)):
            tempLst=[]
            for line in lst:
                tempLst.append(line[i])
            invoice.getDetailsDict()[keysList[i]] = tempLst
        #print(invoice.getDetailsDict())
        file.close()
                
        return invoice
