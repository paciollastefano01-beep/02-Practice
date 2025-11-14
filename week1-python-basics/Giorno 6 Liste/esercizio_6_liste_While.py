# 📝 ESERCIZIO 6: SOMMA E MEDIA

lista_numeri = []

while True:
    numero_scelto = input("Inserisci numero (o 'stop'): ").strip().lower()
    if numero_scelto == "stop":
        break
    else:
        numero_scelto = int(numero_scelto)
        lista_numeri.append(numero_scelto)

somma = 0
for numero in lista_numeri:
    somma = somma + numero
media = somma / len(lista_numeri)

contatore = 0
numeri_sopra_media = []
for i in lista_numeri:
    if i > media:
        contatore = contatore + 1
        numeri_sopra_media.append(i)


print(f"\nNumeri inseriti: {lista_numeri}")
print(f"Somma: {somma}")
print(f"Media: {media}")
print(f"Numeri sopra la media: {contatore} ----> {numeri_sopra_media}")
