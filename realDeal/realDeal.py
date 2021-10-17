from Parser.XmlParser      import XmlParser
from Parser.XmlItemManager import XmlItemManager
from Equations.Noi         import Noi
from pathlib               import Path
from Report.Report         import Report

dataXmlPath     = Path("realDealXml/data.xml")
equationXmlPath = Path("realDealXml/equation.xml")

dataXml      = XmlParser(dataXmlPath)
equationsXml = XmlParser(equationXmlPath)

incomeItems  = XmlItemManager("Income")
incomeItems.appendItems(dataXml.getAllItems('income'))

operatingExpenseItems = XmlItemManager("Operating Expenses")
operatingExpenseItems.appendItems(dataXml.getAllItems('operatingExpense'))

itemManagers = [incomeItems, operatingExpenseItems]

noi = Noi("Net Operating Income")
noi.operatingExpenses = operatingExpenseItems.getItemsSum()
noi.revenue           = incomeItems.getItemsSum()
noi.isEnabled         = equationsXml.findItemEnabled('equation', 'Noi', 'enabled')

equations = [noi]

# Display items listed in XML
report = Report("Real Estate Financial Report", "Real_Estate_Financial_Report.md")

for  im in itemManagers:
    report.addContent("Header", im.name)
    types = im.getTypes()
    for type in types:
        items = im.getItems(type)
        report.addContent("Type", type)
        for item in items:
            report.addContent("Item", item)

# Calculate equations
for equation in equations:
    if equation.isEnabled:
        report.addContent("Equation", equation.name)
        calculations = equation.getCalcString()

        for calculation in calculations:
            report.addContent("Item", calculation)

report.generateMd()