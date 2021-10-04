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

    def getItemsTypePercentages(self) -> dict:
        typePercentages = {}
        if self.numOfItems > 0:
            for item in self._items:
                typePercentages[item.name] = item.typePercent
        return typePercentages

    def getItemsSum(self) -> float:
        sum = 0.00
        for item in self._items:
            sum = sum + item.value
        return sum

    def getTypes(self) -> list:
        types     = []
        typeFound = {}

        # List each item by type
        for itemType in self._items:
            itemTypeSearch = itemType.type

            # Check if the item type has already been checked
            # If not, we can search for the list of this specific item type
            # Then add it to typesDisplayed dictionary when we are done
            if itemTypeSearch not in typeFound:
                types.append(itemTypeSearch)
                typeFound[itemTypeSearch] = "Done"
        return types

    def getItems(self, type: str) -> str:
        items = []

        # List each item by type
        for item in self._items:
            if item.type == type:
                items.append(item.name + "," + str(round(item.value,2)) + "," + str(round(item.typePercent,2)) + "," + str(round(item.percent, 2)))
        return items

    @property
    def numOfItems(self):
        return len(self._items)

    @property
    def name(self):
        return self._name

    def _update(self):
        sum     = 0.0

        # Iterate through items to find the total sum
        for item in self._items:
            sum = sum + item.value

        # Calculate the percentage for each item
        for item in self._items:
            item.percent = (item.value / sum) * 100.00

        # Iterate through items to find what other items have the same type
        # Generate a sum based on the total items of that type
        for currItem in self._items:
            typeSum = 0.0
            for testItem in self._items:
                if currItem.type == testItem.type:
                    typeSum = typeSum + testItem.value
            currItem.typePercent = (currItem.value/typeSum) * 100.00
