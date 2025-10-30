print("=== TEST MAGGIORENNE ===")
eta = int(input("Quanti anni hai? "))
if eta >= 18:
    print("✅ Sei Maggiorenne!")
    print("✅ Puoi Votare!")
    print("✅ Puoi Guidare!")
print("Fine Programma")

print("\n=== CONTROLLO ACCESSO ===")
password_segreta = "Phython123"
password_inserita = input("Inserisci Password: ")
if password_inserita == password_segreta:
    print("✅ ACCESSO CONSENTITO!")
    print("✅ Benvenuto nel sistema")
else:
    print("❌ PASSWORD ERRATA!")
    print("❌ ACCESSO NEGATO!!!")
print("Sistema Chiuso.")

print("\n=== VALUTAZIONE VOTO ===")

voto = int(input("Inserisci Voto (0-10): "))

if voto >= 9:
    print("📊 GIUDIZIO: Ottimo!")
    print("🎉 Eccellente lavoro!")
elif voto >= 7:
    print("📊 GIUDIZIO: Buono")
    print("👍 Bravo, continua così!")
elif voto >= 6:
    print("📊 GIUDIZIO: Sufficiente")
    print("📚 Puoi fare di più!")
elif voto >= 4:
    print("📊 GIUDIZIO: Insufficiente")
    print("⚠️ Devi impegnarti!")
else:
    print("📊 GIUDIZIO: Gravemente insufficiente")
    print("❌ Studia molto di più!")

print("Valutazione completata.")

print("\n=== CONTROLLO ACCESSO DISCOTECA ===")
eta = int(input("Quanti anni hai? "))
if eta >= 18:
    print("✅ Hai l'età giusta!")
    tessera = input("Hai tessera socio (si/no): ")
    if tessera == "si":
        print("🎉 Entri gratis")
        print("Buon divertimento! 🎵")
    else:
        print("💶 Paghi 10$ per entrare")
        print("Buon divertimento! 🎵")
else:
    print("❌ Spiacenti, sei troppo giovene!")
    print("Torna quando avrai 18 anni")

print("\nControllo Terminato.")

print("=== CALCOLO SCONTO ===")

ha_carta = input("Hai carta fedeltà? (si/no): ")
importo = float(input("Importo spesa: "))

if ha_carta == "si":
    if importo > 50:
        print("Complimenti, hai uno sconto del 20%!")
    elif importo > 25:
        print("Ottimo, hai uno sconto del 10%! ")
    else:
        print("Bravo, hai sconto del 5%!")
else:
    print("Mi dispiace ma non hai nessuno sconto")

print("\n=== ACCESSO AREA VIP ===")

# Esempio AND

eta = int(input("Età: "))
vip_pass = input("Hai VIP pass? (si/no): ")

if eta >= 21 and vip_pass == "si":
    print("✅ ACCESSO CONSENTITO!")
    print("Benvenuto nell'area VIP! 🍾")
else:
    print("❌ ACCESSO NEGATO!")
    if eta > 21:
        print("Motivo: Età insufficente")
    if vip_pass != "si":
        print("Motivo: Manca VIP pass")

# Esempio OR
print("\n=== CONTROLLO SCONTO ===")

eta = int(input("Età: "))
studente = input("Sei studente? (si/no): ")

if eta >= 65 or studente == "si":
    print("✅ HAI DIRITTO ALLO SCONTO!")
    print("💰 Sconto 15% applicato!")
else:
    print("Prezzo pieno")

# Esempio NOT

print("\n=== CONTROLLO MANUTENZIONE ===")

in_manutenzione = input("Sistema in manutenzione? (si/no): ")

if not in_manutenzione == "si":
    print("✅ Sistema operativo!")
    print("Accesso consentito")
else:
    print("⚠️ Sistema in manutenzione!")
    print("Riprova più tardi")

# COMBINARE OPERATORI (AND + OR + NOT)

# Promozione: Sconto 25% SE:
# - Cliente ha carta fedeltà
# - E (è studente O età >= 65)
# - E NON ha già usato promozione oggi

ha_carta = input("Carta fedeltà? (Si/No): ")
studente = input("Studente? (Si/No): ")
eta = int(input("Età: "))
usato_promo = input("Già usato promo oggi? (Si/No): ")

if ha_carta == "si" and (studente == "si" or eta >= 65) and not usato_promo == "si":
    print("🎉 SCONTO 25% ATTIVATO!")
else:
    print("Sconto non applicabile")

print("\n=== SISTEMA LOGIN ===")
username = input("Username: ")
password = input("Password: ")
bloccato = input("Account bloccato? (si/no): ")

if username == "admin" and (password == "python123") and not bloccato == "si":
    print("ACCESSO CONSENTITO!")
else:
    print("ACCESSO NEGATO!")
