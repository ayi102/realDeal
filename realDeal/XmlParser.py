import xml.etree.ElementTree as ET
from .Parser import Parser

class XmlParser(Parser):

    def parse(self, file):
        ET.parse(file)
        return file