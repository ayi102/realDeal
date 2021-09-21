from realDeal.XmlParser import XmlParser

class TestXmlParser():

    def setup(self):
        self.p = XmlParser(10)

    def test_doSomething(self):
        assert self.p.do_something() == 42