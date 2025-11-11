# esercizio 3: conta caratteri

frase = (
    input("Scegli una frase: ").strip().lower()
)  # aggiungo correzione della risposta in base all'utente inserisca lettera maiuscola o minuscola

lettera = input("Scegli un lettera: ").strip().lower()

contatore = 0

for i in frase:
    if i == lettera:
        contatore = contatore + 1

print(f"La tua lettera è comparsa {contatore} volte")
