# esercizio 2: Numero più grande

n = float(input("Quanti numeri inserirai? "))

massimo = float(input("Scegli il numero: "))
for i in range(n - 1):
    x = float(input("Scegli un altro numero: "))
    if massimo < x:
        massimo = x
print(f"Il numero massimo che hai scelto è: {massimo}")
