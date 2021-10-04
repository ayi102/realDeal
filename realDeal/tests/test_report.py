from Report.Report import Report
from Parser.XmlItem        import XmlItem
from Parser.XmlItemManager import XmlItemManager

class TestReport():

    def setup(self):
        self.report = Report("Financial Report", "test.md")

    def test_generateMd_when_invoked_then_file_is_generated_with_content(self):
        content    = ['Header', 'Revenue', 'Type', 'Utility', 'Item', 'Rental Income 20.0 50.0 40.0', 'Item', 'Parking 20.0 50.0 40.0', 'Type', 'Fee', 'Item', 'Test 10.0 100.0 20.0']
        ximRevenue = XmlItemManager("revenue")
        item  = XmlItem('Rental Income', 'Utility', 20.00)
        item2 = XmlItem('Parking', 'Utility', 20.00)
        item3 = XmlItem('Test', 'Fee', 10.00)

        ximRevenue.appendItems([item,item2, item3])


        types = ximRevenue.getTypes()
        for type in types:
            items = ximRevenue.getItems(type)
            self.report.addContent("Type", type)
            for item in items:
                self.report.addContent("Item", item)
        self.report.generateMd()