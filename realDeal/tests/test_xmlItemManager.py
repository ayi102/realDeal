from Parser.XmlItem        import XmlItem
from Parser.XmlItemManager import XmlItemManager

class TestXmlItemManager():

    def setup(self):
        self.ximRevenue           = XmlItemManager("revenue")
        self.ximOperatingExpenses = XmlItemManager("operatingExpense")

    def test_getItemsS_when_no_item_is_added_then_the_sum_is_0(self):
        itemSum = self.ximRevenue.getItemsSum()
        assert itemSum == 0.00

    def test_getItemsSum_when_items_are_added_then_the_sum_is_what_was_add(self):
        item = XmlItem('rentalIncome', 'utility', 10.00)
        item2 = XmlItem('ParkingIncome', 'utility', 10.00)
        self.ximRevenue.appendItem(item)
        self.ximRevenue.appendItem(item2)
        itemSum = self.ximRevenue.getItemsSum()
        assert itemSum == 20.00

    def test_getItemsPercentages_when_no_item_is_added_then_the_percent_is_0(self):
        itemPercentages = self.ximRevenue.getItemsPercentages()
        assert itemPercentages == {}

    def test_appendItem_when_Xml_item_is_added_then_the_items_percent_is_updated(self):
        item = XmlItem('rentalIncome', 'utility', 10.00)
        self.ximRevenue.appendItem(item)
        itemPercentages = self.ximRevenue.getItemsPercentages()

        assert itemPercentages['rentalIncome'] == 100.00

    def test_appendItems_when_Xml_items_are_added_then_the_items_percents_and_items_type_percents_are_updated(self):
        item  = XmlItem('rentalIncome', 'utility', 20.00)
        item2 = XmlItem('parking', 'utility', 20.00)
        item3 = XmlItem('test', 'fee', 10.00)

        self.ximRevenue.appendItems([item,item2, item3])

        itemPercentages     = self.ximRevenue.getItemsPercentages()
        itemTypePercentages = self.ximRevenue.getItemsTypePercentages()

        assert itemPercentages['rentalIncome'] == 40.00
        assert itemPercentages['parking']      == 40.00
        assert itemTypePercentages['rentalIncome'] == 50.00