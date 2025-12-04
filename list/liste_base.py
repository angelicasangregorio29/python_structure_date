# liste_base.py

server_list: list [ str ]= ["web01", "db01", "cache01"]

# 1. Aggiungere "backup01" alla fine
server_list.append("backup01")

# 2. Inserire "proxy01" all'inizio
server_list.insert(0, "proxy01")

# 3. Rimuovere "cache01"
server_list.remove("cache01")

# Output finale
print(server_list)
print("Numero server:", len(server_list))