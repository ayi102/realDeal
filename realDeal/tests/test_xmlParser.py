
#from tests.Utilities import *
from XmlParser import XmlParser

class TestXmlParser():

    def setup(self):
        print("Happy")
        # goodDataXmlPath = Utilities.get_absolute_path(
        #     "realDealDataTest/goodData.xml")
        # self.goodData = XmlParser(goodDataXmlPath)

        # badDataXmlPath = Utilities.get_absolute_path(
        #     "realDealDataTest/badData.xml")
        # self.badData = XmlParser(badDataXmlPath)

        # goodEquationXmlPath = Utilities.get_absolute_path(
        #     "realDealDataTest/goodEquations.xml")
        # self.goodEquation = XmlParser(goodEquationXmlPath)

        # badEquationXmlPath = Utilities.get_absolute_path(
        #     "realDealDataTest/badEquations.xml")
        # self.badEquation = XmlParser(badEquationXmlPath)

    # def test_findItemSum_when_there_is_valid_revenue_data_then_sum_is_correct(self):
    #     expectedOutput = 11.0

    #     assert self.goodData.findItemSum('revenue', 'value') == expectedOutput

    # def test_findItemSum_when_there_is_valid_operating_expense_data_then_sum_is_correct(self):
    #     expectedOutput = 6.0

    #     assert self.goodData.findItemSum(
    #         'operatingExpense', 'value') == expectedOutput

    # def test_findItemSum_when_there_is_missing_operating_expense_value_then_exception_thrown(self):
    #     expectedOutput = 6.0

    #     try:
    #         self.badData.findItemSum(
    #             'operatingExpense', 'value') == expectedOutput
    #     except:
    #         assert True

    # def test_findItemSum_when_there_is_invalid_revenue_value_then_exception_thrown(self):
    #     expectedOutput = 6.0

    #     try:
    #         self.badData.findItemSum('revenue', 'value') == expectedOutput
    #     except:
    #         assert True

    # def test_findItemSum_when_there_an_equation_is_enabled_then_detect_it_is(self):
    #     assert self.goodEquation.findItemEnabled('equation', 'NOI', 'enabled') == True

    # def test_findItemSum_when_there_an_equation_is_enabled_then_detect_it_is(self):
    #     assert self.goodEquation.findItemEnabled('equation', 'eq2', 'enabled') == False

    # def test_findItemSum_when_there_is_an_invalid_enabled_variable_then_throw_exception(self):
    #     try:
    #         self.badEquation.findItemEnabled('equation', 'NOI', 'enabled') == True
    #     except:
    #         assert True

    # def test_findItemSum_when_there_is_an_invalid_equation_variable_then_throw_exception(self):
    #     try:
    #         self.badEquation.findItemEnabled('equation', 'eq2', 'enabled') == True
    #     except:
    #         assert True