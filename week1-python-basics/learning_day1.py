name = "Stefano"
count = 23
limit = 50
message = f"Ciao {name}, hai usato {count}/{limit} messaggi"

# Simulare una progress bar
completato = 7
totale = 10

# Calcolo percentuale (metodo chiaro)
percentuale = (completato / totale) * 100
percentuale = int(percentuale)  # Niente decimali

# Crea barra visuale
barre_piene = completato
barre_vuote = totale - completato
barra = "█" * barre_piene + "░" * barre_vuote

print(f"Progress: {barra} {percentuale}%")
# Output: Progress: ███████░░░ 70%

# Calcolo sconto - SUPER CHIARO
prezzo_originale = 29.99
sconto_percentuale = 15

# Calcoli separati (più leggibile)
sconto_euro = prezzo_originale * (sconto_percentuale / 100)
prezzo_finale = prezzo_originale - sconto_euro

# Formattazione semplice per i soldi
print(f"Prezzo originale: €{prezzo_originale}")
print(f"Sconto {sconto_percentuale}%: -€{round(sconto_euro, 2)}")
print(f"Prezzo finale: €{round(prezzo_finale, 2)}")