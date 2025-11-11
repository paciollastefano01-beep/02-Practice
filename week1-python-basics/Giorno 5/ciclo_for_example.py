parola = "computer"
vocali_trovate = 0

for lettera in parola:
    # Controlla se la lettera è una vocale
    if (
        lettera == "a"
        or lettera == "e"
        or lettera == "i"
        or lettera == "o"
        or lettera == "u"
    ):
        vocali_trovate = vocali_trovate + 1  # aumenta il contatore
        print(f"Trovata vocale: {lettera}")

print(f"Totale vocali: {vocali_trovate}")


testo = "ciao"
contatore = 0

for x in testo:
    contatore = contatore + 1

print(contatore)

for numero in range(5):
    print(numero)
