from XmlParser           import XmlParser
from Equations.Noi       import Noi
from pathlib import Path
dataXmlPath     = Path("realDealXml/data.xml")
equationXmlPath = Path("realDealXml/equation.xml")

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