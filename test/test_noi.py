from test.utilities import *
from realDeal.Noi import Noi

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

    def test_calculate_when_calucate_is_executed_then_calculate_noi(self):
        self.noi.revenue           = 2.0
        self.noi.operatingExpenses = 1.0
        assert self.noi.calculate() == 1.0