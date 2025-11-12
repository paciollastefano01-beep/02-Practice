# ESERCIZIO 5: INDOVINA NUMERO

numero_segreto = 7
indovina = 0

while indovina != numero_segreto:
    indovina = int(input("Indovina il numero:"))
    if indovina < numero_segreto:
        print("Troppo Basso!")
        print("Riprova!")
    elif indovina > numero_segreto:
        print("Troppo Alto! ")
        print("Riprova!")

print("Bravo!")
print("Hai indovinato!")
