contatore = 1
while contatore <= 5:
    print(f"Conteggio: {contatore}")
    comando = input(
        "Premi invio per continuare o scrivi 'stop': ").strip().lower()
    if comando == "stop":
        break
    else:
        contatore = contatore + 1


print("Fine!")
