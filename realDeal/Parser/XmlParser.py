from Parser.XmlItem import XmlItem
import xml.etree.ElementTree as ET
from Parser.Parser import Parser

class XmlParser(Parser):

    def __init__(self, file):
        self.file = file
        # create element tree object
        self.root = ET.parse(self.file).getroot()

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

    def getAllItems(self, item):
        listOfItems = []
        for item in self.root.findall(item):
            try:
                name = item.attrib["name"]
            except:
                raise Exception("XML item 'name' property does not exist")
            unit = item.find("unit")
            if unit != None:
                unitText = unit.text
                type = item.find('type')
                if type != None:
                    typeText = type.text
                    value = item.find('value')
                    if value != None:
                        valueText = value.text
                        try:
                            valueFloat = float(valueText)
                        except:
                            raise Exception("XML 'value' property is not a float")
                        listOfItems.append(XmlItem(name, typeText, valueFloat, unitText))
                    else:
                        raise Exception("Xml item 'value' property does not exist")
                else:
                    raise Exception("Xml item 'type' property does not exist")
            else:
                raise Exception("Xml item 'unit' property does not exist")
        return listOfItems