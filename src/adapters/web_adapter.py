'''
Created on 21 dic 2024

@author: afardin
'''
from flask import Flask, request, render_template
from application.tax_calculator import TaxCalculator
from adapters.for_getting_tax_rate_adapter import FixedTaxRateRepository

app = Flask(__name__)

tax_rate_repository = FixedTaxRateRepository()
tax_calculator = TaxCalculator(tax_rate_repository)


@app.route("/", methods=["GET", "POST"])
def index():
    tax = None
    amount = None
    error = None

    if request.method == "POST":
        try:
            amount = float(request.form["amount"])
            tax = tax_calculator.tax_on(amount)
        except ValueError:
            error = "Inserisci un importo valido."
        except Exception as e:
            error = f"Errore durante il calcolo: {e}"

    return render_template("index.html", tax=tax, amount=amount, error=error)


if __name__ == "__main__":
    app.run(debug=True)
