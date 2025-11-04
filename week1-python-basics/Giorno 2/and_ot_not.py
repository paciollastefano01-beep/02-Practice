# AND = ENTRAMBE le condizioni devono essere vere

età = 25
patente = True

if età >= 18 and patente == True:
    print("✅ Puoi guidare")
else:
    print("❌ Non puoi guidare")

# Esempi pratici:
username = input("Username: ")
password = input("Password: ")

# devono essere entrambe corrette per entrare

if username == "admin" and password == "secret123":
    print("Accesso consentito")
else:
    print("Accesso negato")


# OR = AlMENO UNA condizione deve essere vera
giorno = input("Che giorno è? ").lower()

if giorno == "sabato" or giorno == "domenica":
    print("🎉 È weekend!")
else:
    print("💼 È giorno lavorativo")

# Esempio pratico:
metodo_pagamento = input("Paghi con carta o contanti? ").lower()

if metodo_pagamento == "carta" or metodo_pagamento == "contanti":
    print("✅ Pagamento accettato")
else:
    print("❌ Metodo non accettato")


# NOT = inverte True ---->False, False ---->True

piove = False

if not piove:
    print("☀️ Puoi uscire senza ombrello")
else:
    print("☔ Prendi l'ombrello")

# esempio pratico:

ha_pagato = False

if not ha_pagato:
    print("⚠️ Reminder: Devi ancora pagare")
else:
    print("✅ Pagamento ricevuto")

# combinazioni potenti:
# Esempio: Accesso Sistema

eta = int(input("Età: "))
è_studente = input("Sei studente? (si/no): ").lower() == "si"

è_senior = eta >= 65

# Sconto se: studente O senior, Ma deve avere almeno 16 anni

if (è_studente or è_senior) and eta >= 16:
    print("✅ Hai diritto allo sconto!")
    if è_studente:
        print("Sconto studente: 20%")
    elif è_senior:
        print("Sconto senior: 30%")
else:
    print("❌ Nessuno sconto disponibile")
