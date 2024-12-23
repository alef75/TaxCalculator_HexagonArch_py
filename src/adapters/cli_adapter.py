'''
Created on 21 dic 2024

@author: afardin
'''

import argparse
from application.tax_calculator import TaxCalculator
from adapters.for_getting_tax_rate_adapter import FixedTaxRateRepository


def main():
    parser = argparse.ArgumentParser(description="Calcola l'imposta su un importo.")
    parser.add_argument("amount", type=float, help="L'importo su cui calcolare l'imposta.")

    args = parser.parse_args()

    tax_rate_repository = FixedTaxRateRepository()
    tax_calculator = TaxCalculator(tax_rate_repository)

    try:
        tax = tax_calculator.tax_on(args.amount)
        print(f"L'imposta su {args.amount} è {tax}")
    except ValueError:
        print("Importo non valido. Inserisci un numero.")
    except Exception as e:
        print(f"Errore durante il calcolo: {e}")


if __name__ == "__main__":
    main()
