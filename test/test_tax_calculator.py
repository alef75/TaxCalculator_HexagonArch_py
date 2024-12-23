'''
Created on 21 dic 2024

@author: afardin
'''
import unittest
from application.tax_calculator import TaxCalculator
from application.ports.driven.for_getting_tax_rate import ForGettingTaxRates


class TestDynamicRateRepository(ForGettingTaxRates):

    def __init__(self, rate):
        self.rate = rate

    def tax_rate(self, amount: float) -> float:
        return self.rate


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_should_return_zero_for_zero_rate(self):
        zero_rate_repo = TestDynamicRateRepository(0)
        test_tax_calc = TaxCalculator(zero_rate_repo)
        assert test_tax_calc.tax_on(100) == 0

    def test_should_return_the_amount_for_one_rate(self):
        one_rate_repo = TestDynamicRateRepository(1)
        test_tax_calc = TaxCalculator(one_rate_repo)
        assert test_tax_calc.tax_on(100) == 100

    def test_should_return_the_amount_for_any_rate(self):
        one_rate_repo = TestDynamicRateRepository(0.15)
        test_tax_calc = TaxCalculator(one_rate_repo)
        assert test_tax_calc.tax_on(100) == 15


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
