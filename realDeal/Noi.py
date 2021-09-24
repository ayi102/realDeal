from .Equation import Equation

class Noi(Equation):

    def __init__(self, name):
        self._name              = name
        self._isEnabled         = False
        self._operatingExpenses = 0.0
        self._revenue           = 0.0

    @property
    def name(self):
        return self._name

    @property
    def isEnabled(self):
        return self._isEnabled

    @isEnabled.setter
    def isEnabled(self, val):
        self._isEnabled = val

    @property
    def operatingExpenses(self):
        return self._operatingExpenses

    @operatingExpenses.setter
    def operatingExpenses(self, val):
        self._operatingExpenses = val

    @property
    def revenue(self):
        return self._revenue

    @revenue.setter
    def revenue(self, val):
        self._revenue = val

    def calculate(self):
        return (self._revenue - self._operatingExpenses)