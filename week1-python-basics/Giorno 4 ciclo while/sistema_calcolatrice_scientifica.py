# CALCOLATRICE SCIENTIFICA

print("=== CALCOLATRICE SCIENTIFICA ===")

while True:
    print("\n-------------")
    print("1. Addizione")
    print("2. Sottrazione")
    print("3. Moltiplicazione")
    print("4. Divisione")
    print("5. Esci")
    print("-------------")

    scelta = input("\nScegli un numero per l'operazione: ").strip()

    if scelta == "1":
        numero_1 = float(input("Primo Numero: "))
        numero_2 = float(input("Secondo Numero: "))
        print(f"\n{numero_1 + numero_2:.2f}")
    elif scelta == "2":
        numero_1 = float(input("Primo Numero: "))
        numero_2 = float(input("Secondo Numero: "))
        print(f"\n{numero_1 - numero_2:.2f}")
    elif scelta == "3":
        numero_1 = float(input("Primo Numero: "))
        numero_2 = float(input("Secondo Numero: "))
        print(f"\n{numero_1 * numero_2:.2f}")
    elif scelta == "4":
        numero_1 = float(input("Primo Numero: "))
        numero_2 = float(input("Secondo Numero: "))
        if numero_2 == 0:
            print("\nImpossibile dividere per 0!")
        else:
            print(f"\n{numero_1 / numero_2:.2f}")
    elif scelta == "5":
        print("\nArrivederci")
        break
    else:
        print("\nNumero non valido!")
