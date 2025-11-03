print("=" * 40)
print("   CALCOLATORE PREVENTIVO BOT")
print("=" * 40)

nome_azienda = input("Come si chiama l'azienda? ")
settore = input("In quale settore? ").strip().lower()
numero_dipendenti = int(input("Quanti dipendenti hai? "))
budget_mensile = float(input("Qual è il tuo budget a disposizione? "))

costo_base = 500.0
costo_dipendente = 10.0

costo_totale_dipendenti = (
    numero_dipendenti * costo_dipendente
)  # calcolo costo totale dei dipendenti

costo_totale_prima_sconto = costo_base + costo_totale_dipendenti

if settore == "ristorazione":
    sconto = 0.20
elif settore == "e-commerce" or settore == "ecommerce" or settore == "e commerce":   #ho aggiunto modifica per scrittura dell'utente
    sconto = 0.10
elif settore == "servizi":
    sconto = 0.0
else:
    sconto = 0.0

sconto_euro = costo_totale_prima_sconto * sconto
costo_finale = costo_totale_prima_sconto - sconto_euro

if budget_mensile >= costo_finale:
    margine = budget_mensile - costo_finale
    esito = f"✅ Progetto Fattibile: Con margine di €{margine:.2f}"
else:
    deficit = costo_finale - budget_mensile
    esito = f"❌ Budget insufficiente (mancano €{deficit:.2f})"
percento = int(sconto * 100) #aggiunto percentuale sconto

print("======================")
print("PREVENTIVO BOT")
print("======================")
print(f"\nAzienda: {nome_azienda}")
print(f"Settore: {settore.title()}")
print(f"Dipendenti: {numero_dipendenti}")
print("\nCALCOLO COSTI:")
print("--------------")
print(f"Costo base: €{costo_base:.2f}")
print(f"Extra Dipendenti: €{costo_totale_dipendenti:.2f}")
print(f"Subtotale: €{costo_totale_prima_sconto:.2f}")
print(f"Sconto {settore.title()} ({percento}%): -€{sconto_euro:.2f}")
print("--------------")
print(f"TOTALE: €{costo_finale:.2f}")
print(f"\nBudget: €{budget_mensile:.2f}")
print(esito)
