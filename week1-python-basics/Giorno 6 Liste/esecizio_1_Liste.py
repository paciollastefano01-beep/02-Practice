# ESERCIZIO 1: COSTRUIRE UNA LISTA
quantita = int(input("Quanti numeri vuoi analizzare? "))
lista = []

for i in range(quantita):
    numero = int(input("Digita numero: "))
    lista.append(numero)

for i in range(len(lista)):
    print(f"Numero {i + 1}: {lista[i]}")
print(f"\nLista completa: {lista}")
