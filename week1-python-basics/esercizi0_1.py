import math

# 1) INPUT
utenti_totali = 20
percentuale_premium = 0.08
prezzo_mensile = 29.99
costo_api_per_call = 0.03
media_chiamate_giornaliere = 4.5

# 2) COSTANTE
days_in_month = 30

# 3) CALCOLI
premium = round(utenti_totali * percentuale_premium)
revenue_mensile = premium * prezzo_mensile

chiamate_mensili = utenti_totali * media_chiamate_giornaliere * days_in_month
costo_mensile = chiamate_mensili * costo_api_per_call

profitto = revenue_mensile - costo_mensile

break_even_premium = (
    math.ceil(costo_mensile / prezzo_mensile) if prezzo_mensile > 0 else None
)
break_even_percent = (break_even_premium / utenti_totali) if utenti_totali > 0 else None


# 4) OUTPUT FORMATTATO
def eur(x: float) -> str:
    # Formatta stile EU: €1.234,56
    return "€" + f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


print("=======================")
print("BOT CALCULATOR REPORT")
print("=======================")
print(f"Utenti Totali: {utenti_totali:,}")
print(f"Utenti premium: {premium:,} ({percentuale_premium*100:.2f}%)")
print(f"Prezzo mensile: {eur(prezzo_mensile)}")
print(f"Prezzo per API call : {eur(costo_api_per_call)}")
print(f"Media/call giorno: {media_chiamate_giornaliere:.2f}")
print("-----------------------")
print(f"Revenue Mensile: {eur(revenue_mensile)}")
print(f"Costo mensile: {eur(costo_mensile)}")
print(f"Profitto/Perdita: {eur(profitto)}")
if break_even_premium is not None:
    print(
        f"Break-even (premium): {break_even_premium:,} utenti (~{(break_even_percent*100):.2f}%)"
    )
print("=======================")
