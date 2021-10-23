from Equations.Equation import Equation

class VacancyAllowance(Equation):

    def __init__(self, name):
        self._name                 = name
        self._isEnabled            = False
        self._grossScheduledIncome = 0.0
        self._vacancyEstimate      = 3.0

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
    def grossScheduledIncome(self):
        return self._grossScheduledIncome

    @grossScheduledIncome.setter
    def grossScheduledIncome(self, val):
        self._grossScheduledIncome = val

    @property
    def vacancyEstimate(self):
        return self._vacancyEstimate

    @vacancyEstimate.setter
    def vacancyEstimate(self, val):
        self._vacancyEstimate = val

    def calculate(self):
        return round(self._grossScheduledIncome * (self._vacancyEstimate/100),2)

    def getCalcString(self):
        return ["Gross ScheduledIncome,"    + '$' + str(self.grossScheduledIncome),
                "Vacancy Estimate,"         + str(self.vacancyEstimate) + '%',
                "**Vacancy Allowance**," + '$' + str(self.calculate())]