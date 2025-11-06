#Cinema delle condizioni

prezzo_base = 10

eta = int(input("Quanti anni hai? "))
è_studente = input("Sei studente (si/no)? ").strip().lower()
giorno = input("Che giorno è oggi? ").strip().lower()
tessera = input("Hai tessera (si/no)").strip().lower()

if eta <= 16 or è_studente == "si" or giorno == "mercoledi" or tessera == "si":
    nuovo_prezzo = prezzo_base * 0.5

if eta <= 16:
    print("Hai diritto al 50% di sconto")
    print(f"il tuo nuovo prezzo è £ {nuovo_prezzo} perchè hai meno di 17 anni")
elif è_studente == "si":
    print("Hai diritto al 50% di sconto")
    print(f"il tuo nuovo prezzo è £ {nuovo_prezzo} sei studente")
elif giorno == "mercoledi":
    print("Hai diritto al 50% di sconto")
    print(f"il tuo nuovo prezzo è £ {nuovo_prezzo} oggi è mercoledì")
elif tessera == "si":
    print("Hai diritto al 50% di sconto")
    print(f"il tuo nuovo prezzo è £ {nuovo_prezzo} perchè hai tessera socio ")
else:
    print(f"Paghi £ {prezzo_base}")
    print("Non hai diritto allo sconto")





