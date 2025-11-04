importo = float(input("Qual è l'importo? "))
giorno = input("Che giorno è? ")
premium = input("Premium? (si/no): ")

# normalizzo l'output di giorno e di premium
giorno_norm = giorno.strip().lower()
premium_norm = premium.strip().lower()

# applico con if/elif ed else gli sconti in base alle promozioni

sconto_base = 0.0
if importo > 100:
    sconto_base = 0.20
elif sconto_base > 50:
    sconto_base = 0.20
else:
    sconto_base = 0.0

sconto_domenica = 0.0
if giorno_norm == "domenica":
    sconto_domenica = 0.05

sconto_premium = 0.0
if premium_norm == "si":
    sconto_premium = 0.10

# calcolo sconto totale e operazione per calcolare importo prodotto scontato

sconto_totale = sconto_base + sconto_domenica + sconto_premium
totale = importo * (1 - sconto_totale)

# stampo il risultato

print(f"Totale da pagare: {totale:.2f}")
