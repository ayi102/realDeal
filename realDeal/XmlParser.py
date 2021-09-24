import xml.etree.ElementTree as ET
from .Parser import Parser

class XmlParser(Parser):

    def __init__(self, file):
        self.file = file
        # create element tree object
        self.root = ET.parse(self.file).getroot()

    def parse(self):
        revenueSum          = 0.0
        operatingExpenseSum = 0.0

        revenueSum          = self.__findItemSum(root, 'revenue', 'value')
        operatingExpenseSum = self.__findItemSum(root, 'operatingExpense', 'value')

        return {"revenue":revenueSum,
                "operatingExpenses": operatingExpenseSum}

    def findItemSum(self, itemName, itemValue):
        sum = 0.0
        for item in self.root.findall(itemName):
            value = item.find(itemValue)
            if value != None:
                valueText = value.text
                try:
                    sum   = sum + float(valueText)
                except:
                    raise Exception("XML item is not a float value")
            else:
                raise Exception("XML item does not exist")
        return sum

    def findItemEnabled(self):
        return super().findItemEnabled()