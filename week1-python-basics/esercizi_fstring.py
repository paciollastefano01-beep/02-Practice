# Calcolatore sconto:
# - Chiedi prezzo originale
# - Chiedi percentuale sconto
# - Calcola e mostra prezzo finale

prezzo_originale = float(input("Qual'è il prezzo originale?: €"))
percentuale_sconto = float(input("Sconto %: "))

sconto_euro = prezzo_originale * (percentuale_sconto / 100)
prezzo_finale = prezzo_originale - sconto_euro

print(f"Prezzo originale: €{prezzo_originale}")
print(f"Sconto {percentuale_sconto}%: -€{sconto_euro}")
print(f"Prezzo finale: €{prezzo_finale}")

