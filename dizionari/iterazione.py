# iterazione.py
# Esercizio 2.2: Iterazione su dizionari

# Creazione del dizionario utenti
utenti = {
    "alice": "admin",
    "bob": "user",
    "charlie": "guest"
}

# Iterazione sul dizionario e stampa delle coppie
for username, ruolo in utenti.items():
    print(f"Username: {username}, Ruolo: {ruolo}")

# Verifica se "bob" è una chiave presente
print("bob presente:", "bob" in utenti)

# Stampa tutte le chiavi (usernames)
print("Usernames:", utenti.keys())

# Stampa tutti i valori (ruoli)
print("Ruoli:", utenti.values())