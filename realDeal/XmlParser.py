import xml.etree.ElementTree as ET
from .Parser import Parser

class XmlParser(Parser):

    def parse(self, file):

        # create element tree object
        tree = ET.parse(file)
    
        # get root element
        root = tree.getroot()

        # iterate through xml items

        return root.tag