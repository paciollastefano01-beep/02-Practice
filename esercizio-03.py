# Mini calcolatore spesa

articolo_1 = input("Qual'è il nome del primo articolo? ")
prezzo_articolo_1 = float(input("Qual'è il prezzo del primo articolo? "))

articolo_2 = input("Qual'è il nome del secondo articolo? ")
prezzo_articolo_2 = float(input("Qual'è il prezzo del secondo articolo? "))

articolo_3 = input("Qual'è il nome del terzo articolo? ")
prezzo_articolo_3 = float(input("Qual'è il prezzo del terzo articolo? "))

# Ho assegnato variabili e convertito a float (decimali) i prezzi degli articoli

prezzo_totale = prezzo_articolo_1 + prezzo_articolo_2 + prezzo_articolo_3

print("LISTA SPESA")
print("-----------")
print(f"1) {articolo_1}: €{prezzo_articolo_1:.2f}")  #arrotondo tutto a due decimali con 2f
print(f"2) {articolo_2}: €{prezzo_articolo_2:.2f}")
print(f"3) {articolo_3}: €{prezzo_articolo_3:.2f}")
print("-----------")
print(f"Totale: €{prezzo_totale:.2f}")
