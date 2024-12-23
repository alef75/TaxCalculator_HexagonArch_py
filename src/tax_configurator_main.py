'''
Created on 21 dic 2024

@author: afardin
'''
from adapters import cli_adapter
from adapters.web_adapter import app

if __name__ == "__main__":
    # cli_adapter.main()  # Delega l'esecuzione a cli_adapter
    app.run(debug=True)
