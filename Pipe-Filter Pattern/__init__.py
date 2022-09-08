from Pipeline import Pipeline
from Invoice import Invoice
from Filters import CalcDiscountsFilter, CalcFinalPriceFilter, CalcTotalsFilter, ReadFilter, WriteFilter

pipeline = Pipeline([ReadFilter.ReadFilter(), CalcTotalsFilter.CalcTotalsFilter(), CalcDiscountsFilter.CalcDiscountsFilter(), CalcFinalPriceFilter.CalcFinalPriceFilter(), WriteFilter.WriteFilter()])

fileName = input("Enter the path for the file : ")
invoiceObj = Invoice(fileName)
pipeline.generateInvoice(invoiceObj)

