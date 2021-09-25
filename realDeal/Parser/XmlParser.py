import xml.etree.ElementTree as ET
from Parser.Parser import Parser

class XmlParser(Parser):

    def __init__(self, file):
        self.file = file
        # create element tree object
        self.root = ET.parse(self.file).getroot()

    def findItemSum(self, item, itemValue):
        sum = 0.0
        for item in self.root.findall(item):
            value = item.find(itemValue)
            if value != None:
                valueText = value.text
                try:
                    sum   = sum + float(valueText)
                except:
                    raise Exception("XML item is not a float value")
            else:
                raise Exception("XML item attribute does not exist")
        return sum

    def findItemEnabled(self, item, itemName, itemEnabled):
        for item in self.root.findall(item):
            if item.attrib["name"] == itemName:
                value = item.find(itemEnabled)
                if value != None:
                    valueText = value.text
                    if valueText == "True" or valueText == "true":
                        return True
                    else:
                        return False
                else:
                    raise Exception("XML item attribute does not exist")
        raise Exception("XML item does not exist")