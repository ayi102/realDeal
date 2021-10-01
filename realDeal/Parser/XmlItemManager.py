from Parser.XmlItem import XmlItem

class XmlItemManager():

    def __init__(self, name):
        self._name    = name
        self._items   = []

    def appendItem(self, item: XmlItem):
        self._items.append(item)
        self._update()

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
        sum = 0.0
        for item in self._items:
            sum = sum + item.value

        for item in self._items:
            item.percent = (item.value / sum) * 100.00
