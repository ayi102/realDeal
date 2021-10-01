from Parser.XmlItem import XmlItem

class XmlItemManager():

    def __init__(self, name):
        self._name    = name
        self._items   = []

    def appendItem(self, item: XmlItem):
        self._items.append(item)
        self._update()

    def appendItems(self, items: list):
        for item in items:
            self.appendItem(item)

    def getItemsPercentages(self) -> dict:
        percentages = {}
        if self.numOfItems > 0:
            for item in self._items:
                percentages[item.name] = item.percent
        
        return percentages

    def getItemsSum(self) -> float:
        sum = 0.00
        for item in self._items:
            sum = sum + item.value
        
        return sum

    @property
    def numOfItems(self):
        return len(self._items)

    def _update(self):
        sum     = 0.0

        # Iterate through items to find the total sum
        for item in self._items:
            sum = sum + item.value

        # Iterate through items to find what other items have the same type
        # Generate a sum based on the total items 
        for currItem in self._items:

            # Start with a sum that is - the current items value, since we will add it to the sum
            # when we iterate through the list looking for items with the same type
            typeSum = -1 * currItem.value
            for testItem in self._items:
                if currItem.type == testItem.type:
                    typeSum = typeSum + testItem.value
                    

        for item in self._items:
            item.percent = (item.value / sum) * 100.00
