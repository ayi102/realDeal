from Parser.XmlParser           import XmlParser
from Parser.XmlItemManager      import XmlItemManager
from Equations.Noi              import Noi
from Equations.Mortgage         import Mortgage
from Equations.VacancyAllowance import VacancyAllowance
from pathlib                    import Path
from Report.Report              import Report

# File Parsing
dataXmlPath     = Path("realDealXml/data.xml")
equationXmlPath = Path("realDealXml/equation.xml")

dataXml      = XmlParser(dataXmlPath)
equationsXml = XmlParser(equationXmlPath)

# Item Management
incomeItems  = XmlItemManager("Income", False)
incomeItems.appendItems(dataXml.getAllItems('income'))

operatingExpenseItems = XmlItemManager("Operating Expenses", False)
operatingExpenseItems.appendItems(dataXml.getAllItems('operatingExpense'))

mortgageItems = XmlItemManager("Mortgage Items", True)
mortgageItems.appendItems(dataXml.getAllItems("mortgage"))

vacancyItems = XmlItemManager("Vacancy Items", True)
vacancyItems.appendItems(dataXml.getAllItems("vacancyAllowance"))
itemManagers = [incomeItems, operatingExpenseItems, mortgageItems, vacancyItems]

# Equations
noi = Noi("Net Operating Income")
noi.operatingExpenses = operatingExpenseItems.getItemsSum()
noi.revenue           = incomeItems.getItemsSum()
noi.isEnabled         = equationsXml.findItemEnabled('equation', 'Noi', 'enabled')

mortgage             = Mortgage("Mortgage")
mortgage.rate        = mortgageItems.getItemValue('Interest Rate')
mortgage.downPayment = mortgageItems.getItemValue('Down Payment')
mortgage.years       = mortgageItems.getItemValue('Loan Term')
mortgage.loan        = mortgageItems.getItemValue('Loan Amount')
mortgage.isEnabled   = equationsXml.findItemEnabled('equation', 'Mortgage', 'enabled')

vacancyAllowance                      = VacancyAllowance("Vacancy Allowance")
vacancyAllowance.grossScheduledIncome = vacancyItems.getItemValue('Gross Scheduled Income')
vacancyAllowance.vacancyEstimate      = vacancyItems.getItemValue('Vacancy Estimate')
vacancyAllowance.isEnabled            = equationsXml.findItemEnabled('equation', 'VacancyAllowance', 'enabled')

equations = [noi, mortgage, vacancyAllowance]

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