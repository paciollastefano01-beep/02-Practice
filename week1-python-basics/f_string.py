user = "Stefano"
messaggi = 5
limite = 10
percentuale = (messaggi / limite) * 100
print(
    f"""
Ciao {user}!
Hai usato {messaggi}/{limite} messaggi ({percentuale:.0f}%)
Te ne restano {limite - messaggi}.
"""
)

# ESEMPIO REALE 1: Messaggio di benvenuto bot
nome_bot = "AssistentAI"
versione = "2.0"
utente = input("Come ti chiami? ")

benvenuto = f"""
╔════════════════════════════╗
║  Benvenuto {utente}!
║  Sono {nome_bot} v{versione}
║  Come posso aiutarti oggi?
╚════════════════════════════╝
"""
print(benvenuto)

# ESEMPIO REALE 2: Report utilizzo API
chiamate = 156
token_usati = 4500
costo_per_token = 0.000002
costo_totale = token_usati * costo_per_token

report = f"""
📊 REPORT UTILIZZO API
━━━━━━━━━━━━━━━━━━━
Chiamate: {chiamate}
Token: {token_usati:,}
Costo: ${costo_totale:.4f}
━━━━━━━━━━━━━━━━━━━
"""
print(report)

# ESEMPIO REALE 3: Calcolo prezzi con input
servizio = input("Nome servizio: ")
ore = float(input("Ore stimate: "))
tariffa = float(input("Tariffa oraria €: "))

preventivo = f"""
PREVENTIVO {servizio.upper()}
{'=' * 30}
Ore: {ore}
Tariffa: €{tariffa}/ora
{'=' * 30}
TOTALE: €{ore * tariffa:.2f}
(+IVA 22%: €{ore * tariffa * 1.22:.2f})
"""
print(preventivo)
