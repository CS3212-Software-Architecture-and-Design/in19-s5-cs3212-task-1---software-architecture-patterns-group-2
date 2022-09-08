from Filters.AbstractFilter import AbstractFilter
from Invoice import Invoice
import os

class WriteFilter(AbstractFilter):

    def process(self, invoice: Invoice) -> Invoice:

        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        rel_path = "../TextFiles/Output.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        file = open(abs_file_path,"w")

        details_dict = invoice.getDetailsDict()

        finalTotalDiscount_str = "Total discount: " + str(details_dict['TotalDiscount']) + '\n'
        del details_dict['TotalDiscount']
        finalTotalPrice_str = "Total price: " + str(details_dict['FinalTotalPrice'])
        del details_dict['FinalTotalPrice']

        outlst = []

        for i in range(len(details_dict['ItemNames'])):

            temp_lst = []

            for key in details_dict.keys():
                temp_lst.append(str(details_dict[key][i]))
            
            temp_str = ",".join(temp_lst)
            temp_str += '\n'

            outlst.append(temp_str)

        file.writelines(outlst)
        file.write(finalTotalDiscount_str)
        file.write(finalTotalPrice_str)

        file.close()
                
        return invoice