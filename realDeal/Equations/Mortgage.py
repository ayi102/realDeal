from Equations.Equation import Equation

class Mortgage(Equation):

    def __init__(self, name):
        self._name        = name
        self._isEnabled   = False
        self._loan        = 0.0
        self._downPayment = 0.0
        self._rate        = 0.0
        self._years       = 0

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
    def loan(self):
        return self._loan

    @loan.setter
    def loan(self, val):
        self._loan = val

    @property
    def downPayment(self):
        return self._downPayment

    @downPayment.setter
    def downPayment(self, val):
        self._downPayment = val

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, val):
        self._rate = val

    @property
    def years(self):
        return self._years

    @years.setter
    def years(self, val):
        self._years = val

    def calculate(self):
        payments     = self._years * 12
        ratePerMonth = (self._rate / 100.00) / 12.0
        principal    = self._loan - self._downPayment
        numerator    = principal * (ratePerMonth * ((1 + ratePerMonth) ** payments))
        denominator  = ((1 + ratePerMonth) ** payments) - 1

        return round(numerator/denominator,2)

    def getCalcString(self):
        return ["Loan Amount,"   + '$' + str(self.loan),
                "Down Payment,"  + '$' + str(self.downPayment),
                "Loan Term ,"          + str(self.years) + 'Yrs',
                "Interest Rate,"       + str(self.rate)  + '%',
                "**Mortgage Monthly**,"  + '$' + str(self.calculate()),
                "**Mortgage Yearly**,"   + '$' + str(round(self.calculate() * 12.0,2))]