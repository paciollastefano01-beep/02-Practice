giorno = input("Che giorno è? ").strip().lower()
ora = float(input("Orario ? "))
festivo = input("è festivo (si/no)? ").strip().lower()

# definiamo condizioni

è_weekend = giorno == "sabato" or giorno == "domenica"
è_orario_apertura = ora >= 9 and ora <= 19
è_festivo = festivo == "si"

if not è_weekend and è_orario_apertura and not è_festivo:
    print("✅ Negozio APERTO")
else:
    print("🔒 Negozio CHIUSO")

    # specifichiamo perchè è chiuso

    if è_weekend:
        print("- è weekend")
    if not è_orario_apertura:
        print("- Fuori orario (9-19)")
    if è_festivo:
        print("- è giorno festivo")
