# Prima del salvataggio (non formattato)
trovato = False  # Flag iniziale: non l'ho ancora trovato

posti = 0
while posti < 3 and not trovato:
    dove = input("Dove guardo? (cassetto/armadio/tavolo): ")

    if dove == "cassetto":
        print("Trovato!")
        trovato = True  # Alzo la bandierina!
    else:
        print("Non c'è")
        posti = posti + 1

# Dopo il while, controllo la bandierina
if trovato:
    print("Posso usare l'oggetto")
else:
    print("Non l'ho trovato da nessuna parte")
