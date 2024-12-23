'''
Created on 21 dic 2024

@author: afardin
'''
from abc import ABC, abstractmethod

# Interface: ForGettingTaxRates


class ForGettingTaxRates(ABC):
    @abstractmethod
    def tax_rate(self, amount: float) -> float:
        pass
