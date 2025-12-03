# File: ordinamento.py
# Obiettivo: Ordinare liste e verificare esistenza elementi

def analizza_prezzi(lista):
    """Analizza una lista di prezzi e restituisce i risultati principali."""
    prezzi_ordinati = sorted(lista)
    prezzo_min = min(lista)
    prezzo_max = max(lista)
    presente = 23.1 in lista
    count_maggiori_50 = sum(1 for p in lista if p > 50)

    return {
        "originali": lista,
        "ordinati": prezzi_ordinati,
        "minimo": prezzo_min,
        "massimo": prezzo_max,
        "23.1_presente": presente,
        "maggiori_50": count_maggiori_50
    }

def stampa_risultati(risultati):
    """Stampa i risultati dell'analisi in formato leggibile."""
    print("Prezzi originali:", risultati["originali"])
    print("Prezzi ordinati:", risultati["ordinati"])
    print("Minimo:", risultati["minimo"])
    print("Massimo:", risultati["massimo"])
    print("23.1 presente:", risultati["23.1_presente"])
    print("Prezzi > 50:", risultati["maggiori_50"])


# --- Programma principale ---
if __name__ == "__main__":
    prezzi = [45.5, 12.0, 78.3, 23.1, 56.7]
    risultati = analizza_prezzi(prezzi)
    stampa_risultati(risultati)