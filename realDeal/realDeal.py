from Parser.XmlParser      import XmlParser
from Parser.XmlItemManager import XmlItemManager
from Equations.Noi         import Noi
from pathlib               import Path

dataXmlPath     = Path("realDealXml/data.xml")
equationXmlPath = Path("realDealXml/equation.xml")

dataXml      = XmlParser(dataXmlPath)
equationsXml = XmlParser(equationXmlPath)

incomeItems  = XmlItemManager("Income")
incomeItems.appendItems(dataXml.getAllItems('income'))

operatingExpenseItems = XmlItemManager("Operating Expenses")
operatingExpenseItems.appendItems(dataXml.getAllItems('operatingExpense'))

noi = Noi("Noi")
noi.operatingExpenses = operatingExpenseItems.getItemsSum()
noi.revenue           = incomeItems.getItemsSum()
noi.isEnabled         = equationsXml.findItemEnabled('equation', 'Noi', 'enabled')

equations = [noi]

for equation in equations:
    if equation.isEnabled:
        print(equation.calculate())
    else:
        print(equation.name + " is disabled")