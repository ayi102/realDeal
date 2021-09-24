from .XmlParser import XmlParser
from .Noi       import Noi

dataXml      = XmlParser("realDealXml/data.xml")
equationsXml = XmlParser("realDealXml/equation.xml")

noi = Noi("Noi")

noi.operatingExpenses = dataXml.findItemSum('operatingExpense', 'value')
noi.revenue           = dataXml.findItemSum('revenue', 'value')
noi.isEnabled         = equationsXml.findItemEnabled('equation', 'Noi', 'enabled')

equations = [noi]

for equation in equations:
    if equation.isEnabled:
        print(equation.calculate())
    else:
        print(equation.name + " is disabled")