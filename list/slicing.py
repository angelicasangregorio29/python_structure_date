# Esercizio 1.2: Slicing e Accesso
# File: slicing.py
# Obiettivo: Praticare l'accesso agli elementi e lo slicing

# Creazione della lista temperature
temperature = [15, 18, 22, 25, 28, 30, 27, 24, 20]

# Stampare la prima temperatura
print("Prima temperatura:", temperature[0])

# Stampare l'ultima temperatura
print("Ultima temperatura:", temperature[-1])

# Stampare le temperature dalla posizione 2 alla 5 (esclusa)
print("Temperature [2:5]:", temperature[2:5])

# Stampare tutte le temperature con step 2 (saltando una ogni due)
print("Ogni due:", temperature[::2])