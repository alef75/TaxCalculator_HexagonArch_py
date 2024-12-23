'''
Created on 21 dic 2024

@author: afardin
'''

from application.ports.driven.for_getting_tax_rate import ForGettingTaxRates


class FixedTaxRateRepository(ForGettingTaxRates):
    def tax_rate(self, amount: float) -> float:
        return 0.15
