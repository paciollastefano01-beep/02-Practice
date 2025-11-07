# sistema di prenotazione volo completo

eta_passeggero = int(input("Quanti anni hai? "))
if eta_passeggero < 18:
    accompagnato = input("Sei accompagnato? (si/no): ").strip().lower()
    accompagnato_ok = accompagnato == "si"
else:
    accompagnato_ok = True
ha_passaporto = input("Hai passaporto? (si/no): ").strip().lower()
è_vaccinato = input("Sei vaccinato? (si/no): ").strip().lower()
destinazione = input("Destinazione? (nazionale/internazionale): ").strip().lower()
classe_volo = input("Classe? (economy/business/first): ").strip().lower()
è_studente = input("Sei studente? (si/no): ").strip().lower()
ha_carta_fedeltà = input("Hai carta fedeltà? (si/no): ").strip().lower()
bagaglio_kg = float(input("Peso Bagaglio in kg? "))
è_militare = input("Sei militare? ").strip().lower()

ha_passaporto_ok = ha_passaporto == "si"
è_vaccinato_ok = è_vaccinato == "si"
è_studente_ok = è_studente == "si"
ha_carta_fedeltà_ok = ha_carta_fedeltà == "si"
è_militare_ok = è_militare == "si"

può_volare = True
if not ha_passaporto_ok and destinazione == "internazionale":
    può_volare = False
if eta_passeggero < 18 and not accompagnato_ok:
    può_volare = False
if not è_vaccinato_ok and destinazione == "internazionale":
    può_volare = False

if not può_volare:
    print("❌ Volo negato: non rispetta i requisiti necessari.")
else:
    if è_militare_ok or (eta_passeggero >= 70 and classe_volo == "economy"):
        classe_volo = "business"

    if classe_volo == "economy":
        prezzo_nazionale = 200
        prezzo_internazionale = 500
    elif classe_volo == "business":
        prezzo_nazionale = 500
        prezzo_internazionale = 1200
    elif classe_volo == "first":
        prezzo_nazionale = 1000
        prezzo_internazionale = 3000

    if destinazione == "nazionale":
        prezzo_base = prezzo_nazionale
    else:
        prezzo_base = prezzo_internazionale

    prezzo_base_scontato = prezzo_base

    if eta_passeggero < 12:
        prezzo_base_scontato = prezzo_base * 0.5
    elif è_studente_ok and eta_passeggero <= 26:
        prezzo_base_scontato = prezzo_base * 0.7
    elif ha_carta_fedeltà_ok and classe_volo != "first":
        prezzo_base_scontato = prezzo_base * 0.8

    if classe_volo == "first" or è_militare_ok:
        prezzo_bagaglio = 0
    elif classe_volo == "economy":
        if bagaglio_kg <= 20:
            prezzo_bagaglio = 0
        else:
            prezzo_bagaglio = (bagaglio_kg - 20) * 10
    elif classe_volo == "business":
        if bagaglio_kg <= 30:
            prezzo_bagaglio = 0
        else:
            prezzo_bagaglio = (bagaglio_kg - 30) * 8

    prezzo_finale = prezzo_base_scontato + prezzo_bagaglio

    print("=========================")
    print("SISTEMA PRENOTAZIONE VOLO")
    print("=========================")
    print("")
    print("✅ Puoi volare: tutti i requisiti sono rispettati.")
    print(f"Classe finale volo: {classe_volo}")
    print(f"Prezzo Base Volo:  €{prezzo_base}")
    if prezzo_base_scontato != prezzo_base:
        print(f"Prezzo Base Scontato: €{prezzo_base_scontato}")
    else:
        print("Nessuno Sconto applicabile")
    print(f"Costo del bagaglio: €{prezzo_bagaglio}")
    print(f"Prezzo Finale:  €{prezzo_finale}")
    print("")
    print("\n=========================")
    print("BUON VIAGGIO")
    print("GRAZIE PER AVERCI SCELTO")
    print("=========================")
