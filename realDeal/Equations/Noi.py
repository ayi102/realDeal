from Equations.Equation import Equation

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
        return round((self._revenue - self._operatingExpenses),2)

    def getCalcString(self):
        return ["Real Estate Revenue,"      + '$' + str(self.revenue),
                "Operating Expenses,"       + '$' + str(self.operatingExpenses),
                "**Net Operating Income**," + '$' + str(self.calculate())]

    def calculateProjections(self, annualRevenueIncrease, annualExpenseIncrease, years):

        calculations = []
        for i in range(0, years):
            calculations.append(self.calculate())
            self._revenue = self._revenue * (1.0 + annualRevenueIncrease/100.0)
            self._operatingExpenses = self._operatingExpenses * (1.0 + annualExpenseIncrease/100.0)

        return calculations

    def getCalcProjectString(self, calculations):
        cnt = 1
        projection = []
        for noiCalc in calculations:
            projection.append("Year " + str(cnt))
            projection.append("$ " + str(noiCalc))
            cnt = cnt + 1

        return projection
