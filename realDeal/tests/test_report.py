from Report.Report         import Report
from Parser.XmlItem        import XmlItem
from Parser.XmlItemManager import XmlItemManager
from Equations.Noi         import Noi

class TestReport():

    def setup(self):
        self.report = Report("Financial Report", "test.md")
        self.noi    = Noi("Net Operating Income")

    def test_generateMd_when_invoked_then_file_is_generated_with_content(self):

        ximRevenue        = XmlItemManager("Income")
        operatingExpenses = XmlItemManager("Operating Expenses")
        rev1       = XmlItem('Rental Income', 'Utility', 20.00)
        rev2       = XmlItem('Parking', 'Utility', 20.00)
        oe1        = XmlItem('Test', 'Fee', 10.00)

        ximRevenue.appendItems([rev1,rev2])
        operatingExpenses.appendItem(oe1)

        self.report.addContent("Header", ximRevenue.name)
        types = ximRevenue.getTypes()
        for type in types:
            items = ximRevenue.getItems(type)
            self.report.addContent("Type", type)
            for item in items:
                self.report.addContent("Item", item)

        self.report.addContent("Header", operatingExpenses.name)
        expenses = operatingExpenses.getTypes()
        for expense in expenses:
            items = operatingExpenses.getItems(expense)
            self.report.addContent("Type", expense)
            for item in items:
                self.report.addContent("Item", item)

        self.noi.revenue           = ximRevenue.getItemsSum()
        self.noi.operatingExpenses = operatingExpenses.getItemsSum()
        self.report.addContent("Equation", self.noi.name)
        calculations = self.noi.getCalcString()

        for calculation in calculations:
            self.report.addContent("Item", calculation)

        self.report.generateMd()