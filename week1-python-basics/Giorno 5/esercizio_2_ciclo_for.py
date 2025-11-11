# esercizio 2: Numero più grande

n = int(input("Quanti numeri inserirai? "))

massimo = int(input("Scegli il numero: "))
for i in range(n - 1):
    x = int(input("Scegli un altro numero: "))
    if massimo < x:
        massimo = x
print(f"Il numero massimo che hai scelto è: {massimo}")
