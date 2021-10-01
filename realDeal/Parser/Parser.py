from abc import ABC, abstractmethod

class Parser(ABC):

    @abstractmethod
    def __init__(self, file):
        self.file = file

    @abstractmethod
    def findItemEnabled(self, item, itemName, itemEnabled):
        pass

    @abstractmethod
    def getAllItems(self, item, attribute):
        pass