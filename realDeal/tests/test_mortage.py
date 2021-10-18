from Equations.Mortgage import Mortgage

class TestMortgage():

    def setup(self):
        self.morgtage             = Mortgage("Estimated Mortgage")
        self.morgtage.downPayment = 20000.00
        self.morgtage.loan        = 260000.00
        self.morgtage.rate        = 3.13
        self.morgtage.years       = 30


    def test_calculate_when_calculate_is_executed_then_calculate_mortgage(self):
        assert self.morgtage.calculate() == 1028.75

    def test_getCalcString_when_string_is_requested_then_the_correct_string_is_returned(self):
        assert self.morgtage.getCalcString() == ["Loan Amount ($),"   + str(self.morgtage.loan),
                                                "Down Payment ($),"   + str(self.morgtage.downPayment),
                                                "Loan Term (Years),"  + str(self.morgtage.years),
                                                "Interest Rate (%),"  + str(self.morgtage.rate),
                                                "**Morgtage**,"       + str(self.morgtage.calculate())]