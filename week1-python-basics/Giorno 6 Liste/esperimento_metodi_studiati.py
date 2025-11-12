# Costruiamo una lista passo-passo
lista = []
print(f"Inizio: {lista}")

# Aggiungiamo elementi
lista.append("primo")
print(f"Dopo append('primo'): {lista}")

lista.append("secondo")
print(f"Dopo append('secondo'): {lista}")

lista.insert(0, "zero")
print(f"Dopo insert(0, 'zero'): {lista}")

# Rimuoviamo
lista.remove("primo")
print(f"Dopo remove('primo'): {lista}")

ultimo = lista.pop()
print(f"Dopo pop(): {lista}, rimosso: {ultimo}")
