from Equations.VacancyAllowance import VacancyAllowance

class TestVacancyAllowance():

    def setup(self):
        self.vacancyAllowance = VacancyAllowance("VacancyAllowance")

    def test_name_when_va_constructed_then_name_is_set(self):
        assert self.vacancyAllowance.name == "VacancyAllowance"

    def test_isEnabled_when_isEnabled_is_set_to_true_then_isEnabled_is_true(self):
        self.vacancyAllowance.isEnabled = True
        assert self.vacancyAllowance.isEnabled == True

    def test_isEnabled_when_isEnabled_is_set_to_false_then_isEnabled_is_false(self):
        self.vacancyAllowance.isEnabled = False
        assert self.vacancyAllowance.isEnabled == False

    def test_gsi_when_set_then_get_is_valid(self):
        self.vacancyAllowance.grossScheduledIncome = 1.0
        assert self.vacancyAllowance.grossScheduledIncome == 1.0

    def test_ve_when_set_then_get_is_valid(self):
        self.vacancyAllowance.vacancyEstimate = 2.0
        assert self.vacancyAllowance.vacancyEstimate == 2.0

    def test_calculate_when_calculate_is_executed_then_calculate_vacancyAllowance(self):
        self.vacancyAllowance.vacancyEstimate      = 2.0
        self.vacancyAllowance.grossScheduledIncome = 100.0
        assert self.vacancyAllowance.calculate() == 2.0

    def test_getCalcString_when_string_is_requested_then_the_correct_string_is_returned(self):
        self.vacancyAllowance.vacancyEstimate      = 2.0
        self.vacancyAllowance.grossScheduledIncome = 100.0

        assert self.vacancyAllowance.getCalcString() ==["Gross Scheduled Income,$100.0",
                                                        "Vacancy Estimate,2.0%",
                                                        "**Vacancy Allowance**,$2.0"]