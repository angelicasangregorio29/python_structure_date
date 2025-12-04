# lista_dizionari.py

# Creazione della lista di prodotti (lista di dizionari)
products: list[dict[str , str| int | float  ]] = [
    {"nome": "Laptop", "prezzo": 899.99, "quantita": 5},
    {"nome": "Mouse", "prezzo": 25.50, "quantita": 50},
    {"nome": "Tastiera", "prezzo": 75.00, "quantita": 30},
    {"nome": "Monitor", "prezzo": 299.99, "quantita": 15}
]

# Stampare solo i prodotti con prezzo superiore a 100
print("Prodotti > 100€:")
for product in products:
    if product["prezzo"] > 100:
        print(f"- {product['nome']}: €{product['prezzo']:.2f}")

# Calcolare il valore totale dell'inventario
valore_totale = 0
for product in products:
    valore_totale += product["prezzo"] * product["quantita"]

print(f"\nValore totale inventario: €{valore_totale:.2f}")