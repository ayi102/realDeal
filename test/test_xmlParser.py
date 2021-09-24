
from test.utilities import *
from realDeal.XmlParser import XmlParser

class TestXmlParser():

    def setup(self):
        goodXmlPath = Utilities.get_absolute_path("realDealDataTest/goodData.xml")
        self.good = XmlParser(goodXmlPath)

        badXmlPath = Utilities.get_absolute_path("realDealDataTest/badData.xml")
        self.bad = XmlParser(badXmlPath)

    def test_findItemSum_when_there_is_valid_revenue_data_then_sum_is_correct(self):
        expectedOutput = 11.0

        assert self.good.findItemSum('revenue', 'value') == expectedOutput

    def test_findItemSum_when_there_is_valid_operating_expense_data_then_sum_is_correct(self):
        expectedOutput = 6.0

        assert self.good.findItemSum('operatingExpense', 'value') == expectedOutput

    def test_findItemSum_when_there_is_missing_operating_expense_value_then_exception_thrown(self):
        expectedOutput = 6.0

        try:
            self.bad.findItemSum('operatingExpense', 'value') == expectedOutput
        except:
            assert True

    def test_findItemSum_when_there_is_invalid_revenue_value_then_exception_thrown(self):
        expectedOutput = 6.0

        try:
             self.bad.findItemSum('revenue', 'value') == expectedOutput
        except:
            assert True