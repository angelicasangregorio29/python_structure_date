# liste_base.py

server = ["web01", "db01", "cache01"]

# 1. Aggiungere "backup01" alla fine
server.append("backup01")

# 2. Inserire "proxy01" all'inizio
server.insert(0, "proxy01")

# 3. Rimuovere "cache01"
server.remove("cache01")

# Output finale
print(server)
print("Numero server:", len(server))