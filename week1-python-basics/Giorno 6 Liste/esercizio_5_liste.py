# ESERCIZIO 5: LISTA FILTRATA
numeri_lista = []
for i in range(5):
    numeri_utente = int(input(f"Numero {i + 1}: "))
    numeri_lista.append(numeri_utente)

lista_grandi = []
for maggiori in numeri_lista:
    if maggiori > 10:
        lista_grandi.append(maggiori)

print(f"Lista originale: {numeri_lista}")
print(f"Numeri maggiori di 10: {lista_grandi}")
print(f"Trovati {len(lista_grandi)} maggiori di 10")
