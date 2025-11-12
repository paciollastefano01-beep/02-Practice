# Completa questo codice
numero_magico = 7
indovinato = False

while not indovinato:
    tentativo = int(input("Indovina: "))
    if tentativo == numero_magico:
        indovinato = True
        print("Bravo!")
    else:
        print("Riprova")

if indovinato:
    print("Hai Vinto!")