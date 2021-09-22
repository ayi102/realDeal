
from test.utilities import *
from realDeal.XmlParser import XmlParser

class TestXmlParser():

    def setup(self):
        self.p = XmlParser(10)

    def test_parse(self):
        expectedOutput = {"operatingExpenses":0.0,
                          "revenue":0.0}
        xmlPath = Utilities.get_absolute_path("realDealDataTest/data.xml")
        assert self.p.parse(xmlPath) == expectedOutput