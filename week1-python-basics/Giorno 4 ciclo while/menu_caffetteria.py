# menu caffetteria
print("=== BENVENUTO ===")
print()

ordini = 0

while True:
    print("--- MENU ---")
    print()
    print("1. Caffè")
    print("2. Cioccolata Calda")
    print("3. Latte")
    print("4. Cappuccino")
    print("5. Esci")

    scelta = input("\nBuongiorno, cosa gradisce da bere? ").strip()
    if scelta == "1":
        ordini = ordini + 1
        print("\nPerfetto ti porto subito un bel caffè!")
    elif scelta == "2":
        ordini = ordini + 1
        print("\nOttimo, che cioccolata calda sia!")
    elif scelta == "3":
        ordini = ordini + 1
        print("\nGrande, il latte arriva subito!")
    elif scelta == "4":
        ordini = ordini + 1
        print("\nUn bel cappuccino per il signore!")
    elif scelta == "5":
        print("\nArrivederci")
        print(f"Hai ordinato {ordini} bevande!")
        break
    else:
        print("Scelta non valida!")
        print("\nPer favore scegli un numero compreso tra 1 e 5")
