punteggio = int(input("Quale punteggio? "))
bonus = input("Hai presenza bonus? (si/no)")

if bonus == "si":
    punteggio = punteggio + 5

if punteggio > 100:
    punteggio = 100

if punteggio >= 90:
    voto_lettera = "A"
elif punteggio >= 80:
    voto_lettera = "B"
elif punteggio >= 70:
    voto_lettera = "C"
elif punteggio >= 60:
    voto_lettera = "D"
else:
    voto_lettera = "F"

ultima_cifra = punteggio % 10

if ultima_cifra >= 7 and ultima_cifra <= 9:
    voto_lettera = f"{voto_lettera}+"

print(voto_lettera)