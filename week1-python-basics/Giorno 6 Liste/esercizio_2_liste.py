lista_spesa = []

while True:
    prodotto = (
        input(
            "Scegli il prodotto da aggiungere alla lista della spesa o scrivi 'stop' per interrompere: "
        )
        .strip()
        .lower()
    )
    if prodotto == "stop":
        break
    else:
        lista_spesa.append(prodotto)

for i in range(len(lista_spesa)):
    print(f"\nProdotto {i + 1} = {lista_spesa[i]}")

print(f"\nHai scelto {len(lista_spesa)} prodotti")
print(f"\nLista completa: {lista_spesa}")
