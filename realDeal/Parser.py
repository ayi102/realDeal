from abc import ABC, abstractmethod

class Parser(ABC):

    @abstractmethod
    def __init__(self, file):
        self.file = file

    @abstractmethod
    def parse(self):
        pass

    @abstractmethod
    def findItemSum(self):
        pass