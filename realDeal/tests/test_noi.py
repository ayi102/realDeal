from Equations.Noi import Noi

class TestNoi():

    def setup(self):
        self.noi = Noi("Noi")

    def test_name_when_noi_constructed_then_name_is_set(self):
        assert self.noi.name == "Noi"

    def test_isEnabled_when_isEnabled_is_set_to_true_then_isEnabled_is_true(self):
        self.noi.isEnabled = True
        assert self.noi.isEnabled == True

    def test_isEnabled_when_isEnabled_is_set_to_false_then_isEnabled_is_false(self):
        self.noi.isEnabled = False
        assert self.noi.isEnabled == False

    def test_operatingExpenses_when_set_then_get_is_valid(self):
        self.noi.operatingExpenses = 1.0
        assert self.noi.operatingExpenses == 1.0

    def test_revenue_when_set_then_get_is_valid(self):
        self.noi.revenue = 2.0
        assert self.noi.revenue == 2.0

    def test_calculate_when_calculate_is_executed_then_calculate_noi(self):
        self.noi.revenue           = 2.0
        self.noi.operatingExpenses = 1.0
        assert self.noi.calculate() == 1.0

    def test_getCalcString_when_string_is_requested_then_the_correct_string_is_returned(self):
        self.noi.revenue           = 2.0
        self.noi.operatingExpenses = 1.0

        assert self.noi.getCalcString() ==[("Real Estate Revenue,$2.0"),
                                            ("Operating Expenses,$1.0"),
                                            ("**Net Operating Income**,$1.0")]

    def test_calculateProjects_when_values_are_valid_then_list_is_valid(self):
        self.noi.revenue = 258408.0
        self.noi.operatingExpenses = 122820.0

        assert [135588.0, 139655.64, 143845.31, 148160.67, 152605.49] == self.noi.calculateProjections(3,3,5)

    def test_getCalcProjectString_when_values_are_valid_then_get_correct_string(self):
        self.noi.revenue = 258408.0
        self.noi.operatingExpenses = 122820.0
        calcs = self.noi.calculateProjections(3,3,5)
        assert ['Year 1', '$ 135588.0', 'Year 2', '$ 139655.64', 'Year 3', '$ 143845.31', 'Year 4', '$ 148160.67', 'Year 5', '$ 152605.49'] == self.noi.getCalcProjectString(calcs)

