# Sisitema login con almeno 3 tentativi

username_corretto = "admin"
password_corretta = "python123"

tentativi = 0
max_tentativi = 3
accesso_consentito = False  # flag per tracciare il successo

print("=== SISTEMA BANCARIO ===")

while tentativi < max_tentativi and not accesso_consentito:
    print(f"\nTentativo {tentativi + 1} di {max_tentativi}")

    username = input("Username: ")
    password = input("Password: ")

    if username == username_corretto and password == password_corretta:
        accesso_consentito = True  # cambia il flag
        print("✅ Accesso consentito!")
    else:
        tentativi = tentativi + 1  # incrementa solo se sbaglia

        if tentativi < max_tentativi:
            rimasti = max_tentativi - tentativi
            print(f"❌ Credenziali errate. {rimasti} tentativi rimasti")
        else:
            print("🔒 Account bloccato! Contatta l'assistenza.")

# dopo il while

if accesso_consentito:
    print("\nBenvenuto nel tuo conto bancario!")
    print("Saldo: €1,234.56")
else:
    print("\nAccesso negato.")

