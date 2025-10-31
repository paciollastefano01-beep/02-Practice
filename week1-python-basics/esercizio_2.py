# ===========================
# DYNAMIC PRICING SYSTEM (BASE)
# ===========================

# 1) DEFINIZIONE PIANI (solo variabili)

piano_free_nome = "FREE"
piano_basic_nome = "BASIC"
piano_pro_nome = "PRO"

prezzo_free = 0.00
prezzo_basic = 9.99
prezzo_pro = 29.99

limite_free = 100
limite_basic = 1000
limite_pro = 5000

features_free = "• Messaggi limitati • Nessun supporto"
features_basic = "• Cronologia • Supporto email"
features_pro = "• Tutte le feature • Supporto prioritario"

# 2) INPUT UTENTE

piano_scelto = "PRO"
licenze = 7

# 3) SELEZIONA PARAMETRI DEL PIANO
prezzo_unitario = 0.0
limite = 0
features_sel = ""
piano_upper = piano_scelto.upper()

if piano_upper == "FREE":
    prezzo_unitario = prezzo_free
    limite = limite_free
    features_sel = features_free
elif piano_upper == "BASIC":
    prezzo_unitario = prezzo_basic
    limite = limite_basic
    features_sel = features_basic
elif piano_upper == "PRO":
    prezzo_unitario = prezzo_pro
    limite = limite_pro
    features_sel = features_pro
else:
    print("Errore: piano non valido (usa FREE, BASIC o PRO).")

# 4) CALCOLI
subtotale = licenze * prezzo_unitario

sconto_percent = 0.0
if licenze >= 10:
    sconto_percent = 0.20
elif licenze >= 5:
    sconto_percent = 0.10

sconto_valore = subtotale * sconto_percent
totale = subtotale - sconto_valore
risparmio = sconto_valore

# 5) OUTPUT FORMATTATO
print("==================")
print("PREVENTIVO BOT AI")
print("==================")
print(f"Piano: {piano_upper}")
print(f"Licenze: {licenze}")
print(f"Prezzo unitario: €{prezzo_unitario:.2f} ")
print(f"Limite messaggi: {limite}/mese")
print(f"Feature: {features_sel}")
print(f"Subtotale: €{subtotale:.2f}")

# Mostra lo sconto solo se > 0
if sconto_percent > 0:
    percent_label = int(sconto_percent * 100)
    print(f"Sconto ({percent_label}%): -€{sconto_valore:.2f}")
else:
    print("Sconto: €0.00")

print(f"TOTALE: €{totale:.2f}")
print(f"Risparmio: €{risparmio:.2f}")
print("==================")
