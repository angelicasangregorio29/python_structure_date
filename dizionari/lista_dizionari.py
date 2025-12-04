# lista_dizionari.py

# Creazione della lista di prodotti (lista di dizionari)
prodotti = [
    {"nome": "Laptop", "prezzo": 899.99, "quantita": 5},
    {"nome": "Mouse", "prezzo": 25.50, "quantita": 50},
    {"nome": "Tastiera", "prezzo": 75.00, "quantita": 30},
    {"nome": "Monitor", "prezzo": 299.99, "quantita": 15}
]

# Stampare solo i prodotti con prezzo superiore a 100
print("Prodotti > 100€:")
for prodotto in prodotti:
    if prodotto["prezzo"] > 100:
        print(f"- {prodotto['nome']}: €{prodotto['prezzo']:.2f}")

# Calcolare il valore totale dell'inventario
valore_totale = 0
for prodotto in prodotti:
    valore_totale += prodotto["prezzo"] * prodotto["quantita"]

print(f"\nValore totale inventario: €{valore_totale:.2f}")