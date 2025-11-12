# Sistema login con 3 tentativi

password_corretta = "python123"
tentativi = 3

while tentativi > 0:
    password_utente = input("Password: ")
    tentativi = tentativi - 1
    if password_utente == password_corretta:
        print("\nAccesso Consentito!")
        break
    else:
        if tentativi == 1:
            print(f"\nHai ancora {tentativi} tentativo a disposizione")
        elif tentativi == 0:
            print("\nAccesso Bloccato")
            print("Hai esaurito i tuoi tentativi a disposizione")
        else:
            print(f"\nHai ancora {tentativi} tentativi a disposizione")
