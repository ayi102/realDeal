from abc import ABC, abstractmethod

class Equation(ABC):

    @abstractmethod
    def __init__(self, name):
        self._name      = name
        self._isEnabled = False

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def isEnabled(self):
        pass

    @isEnabled.setter
    @abstractmethod
    def isEnabled(self, val):
        pass

    @abstractmethod
    def calculate(self):
        pass

    @abstractmethod
    def getCalcString(self):
        pass