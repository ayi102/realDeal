import os
from realDeal.XmlParser import XmlParser

class TestXmlParser():

    def setup(self):
        self.p = XmlParser(10)

    def test_doSomething(self):
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(THIS_FOLDER, 'realDealDataTest\\data.xml')
        assert self.p.parse(my_file) == "RealDealData"