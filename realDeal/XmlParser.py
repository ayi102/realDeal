import xml.etree.ElementTree as ET
from .Parser import Parser

class XmlParser(Parser):

    def parse(self, file):
        revenueSum          = 0.0
        operatingExpenseSum = 0.0

        # create element tree object
        root = ET.parse(file).getroot()

        revenueSum          = self.__findItemSum(root, 'revenue', 'value')
        operatingExpenseSum = self.__findItemSum(root, 'operatingExpense', 'value')

        return {"revenue":revenueSum,
                "operatingExpenses": operatingExpenseSum}

    def __findItemSum(self, xmlRoot, itemName, itemAttribute):
        sum = 0.0
        for item in xmlRoot.findall(itemName):
            value = item.find(itemAttribute).text
            sum   = sum + float(value)

        return sum