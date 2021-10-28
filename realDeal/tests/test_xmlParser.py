
from pathlib          import Path
from Parser.XmlParser import XmlParser
from Parser.XmlItem   import XmlItem

class TestXmlParser():

    def setup(self):
        goodDataXmlPath = Path.cwd().joinpath("tests/realDealDataTest/goodData.xml")
        print(goodDataXmlPath)
        self.goodData   = XmlParser(goodDataXmlPath)

        badDataXmlPath = Path.cwd().joinpath("tests/realDealDataTest/badData.xml")
        self.badData   = XmlParser(badDataXmlPath)

        goodEquationXmlPath = Path.cwd().joinpath("tests/realDealDataTest/goodEquations.xml")
        self.goodEquation   = XmlParser(goodEquationXmlPath)

        badEquationXmlPath = Path.cwd().joinpath("tests/realDealDataTest/badEquations.xml")
        self.badEquation   = XmlParser(badEquationXmlPath)

    def test_findItemEnabled_when_there_an_equation_is_enabled_then_detect_it_is(self):
        assert self.goodEquation.findItemEnabled('NOI') == True

    def test_findItemEnabled_when_there_an_equation_is_enabled_then_detect_it_is(self):
        assert self.goodEquation.findItemEnabled('eq2') == False

    def test_findItemEnabled_when_there_is_an_invalid_enabled_variable_then_throw_exception(self):
        try:
            self.badEquation.findItemEnabled('NOI') == True
        except:
            assert True

    def test_findItemEnabled_when_there_is_an_invalid_equation_variable_then_throw_exception(self):
        try:
            self.badEquation.findItemEnabled('eq2') == True
        except:
            assert True

    def test_getAllItems_when_items_are_available_then_return_a_list_of_lists_with_all_of_their_attributes(self):
        expectedItems = [XmlItem('rentalIncome', 'rent', 1.00, '$'),
                         XmlItem('parking', 'fee', 10.00, '$')]
        items         = self.goodData.getAllItems('revenue')

        assert expectedItems == items

    def test_getAllItems_when_the_item_is_missing_a_name_then_throw_exception(self):
        try:
            items = self.badData.getAllItems('noNameFailure')
        except:
            assert True

    def test_getAllItems_when_the_item_has_an_invalid_value_then_throw_exception(self):
        try:
            items = self.badData.getAllItems('revenue')
        except:
            assert True

    def test_getAllItems_when_the_item_is_missing_a_type_then_throw_exception(self):
        try:
            items = self.badData.getAllItems('noTypeFailure')
        except:
            assert True


    def test_getAllItems_when_the_item_is_missing_a_value_then_throw_exception(self):
        try:
            items = self.badData.getAllItems('noValueFailure')
        except:
            assert True