'''
Created on 21 dic 2024

@author: afardin
'''
from abc import ABC, abstractmethod


class ForCalculatingTaxes(ABC):
    @abstractmethod
    def tax_on(self, amount: float) -> float:
        pass
