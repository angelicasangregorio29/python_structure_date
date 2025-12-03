# Esercizio 1.2: Slicing e Accesso
# File: slicing.py
# Obiettivo: Praticare l'accesso agli elementi e lo slicing

# Creiamo una lista di temperature
temperature = [15, 18, 22, 25, 28, 30, 27, 24, 20]

# Accesso diretto al primo elemento della lista
# Gli indici in Python partono da 0, quindi temperature[0] è il primo valore
print("Prima temperatura:", temperature[0])

# Accesso diretto all'ultimo elemento della lista
# L'indice -1 in Python indica l'ultimo elemento
print("Ultima temperatura:", temperature[-1])

# Slicing: estraiamo gli elementi dalla posizione 2 alla 5 (esclusa)
# Ricorda: l'indice iniziale è incluso, quello finale è escluso
print("Temperature [2:5]:", temperature[2:5])

# Slicing con step: prendiamo tutti gli elementi saltando uno ogni due
# La sintassi è lista[inizio:fine:step], qui step=2
print("Ogni due:", temperature[::2])