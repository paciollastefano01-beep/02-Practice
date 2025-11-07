# sistema parcheggio

è_residente = input("Sei residente(si/no)? ").strip().lower()
ha_permesso = input("Hai permesso speciale (si/no)? ").strip().lower()
è_disabile = input("Hai disabilità (si/no)? ").strip().lower()
ore_sosta = float(input("Quante ore devi sostare? "))

residente_ok = è_residente == "si"
permesso_ok = ha_permesso == "si"
disabile_ok = è_disabile == "si"
prezzo_finale_permesso = ore_sosta * 2

if residente_ok or disabile_ok:
    print("Parcheggio Gratis")
elif permesso_ok:
    print(f"Paghi 2£/l'ora per {ore_sosta} ore")
    print(f"Prezzo Finale: £ {prezzo_finale_permesso}")
if not (residente_ok or disabile_ok or permesso_ok):
    print("Non puoi parcheggiare")
