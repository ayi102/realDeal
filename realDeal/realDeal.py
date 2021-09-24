from XmlParser import XmlParser
from Noi       import Noi
from Utilities import *

dataXmlPath     = Utilities.get_absolute_path(
                    "realDealXml/data.xml")
equationXmlPath = Utilities.get_absolute_path(
                    "realDealXml/equation.xml")

dataXml      = XmlParser(dataXmlPath)
equationsXml = XmlParser(equationXmlPath)

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