# liste_base.py

# Creazione della lista iniziale
server = ["web01", "db01", "cache01"]

# Aggiungere "backup01" alla fine
server.append("backup01")

# Inserire "proxy01" all'inizio (indice 0)
server.insert(0, "proxy01")

# Rimuovere "cache01"
server.remove("cache01")

# Stampare la lista finale
print(server)

# Stampare la lunghezza della lista
print("Numero server:", len(server))


