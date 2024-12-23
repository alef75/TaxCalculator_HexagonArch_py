'''
Created on 21 dic 2024

@author: afardin
'''

from application.ports.driven.for_getting_tax_rate import ForGettingTaxRates
from application.ports.driving.for_calculating_taxes import ForCalculatingTaxes


class TaxCalculator(ForCalculatingTaxes):
    def __init__(self, tax_rate_repository: ForGettingTaxRates):
        self.tax_rate_repository = tax_rate_repository

    def tax_on(self, amount: float) -> float:
        return amount * self.tax_rate_repository.tax_rate(amount)
