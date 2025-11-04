#sistema login banca

username = "admin"
password = "sedano123"
pin = "98765"

username_utente = input("Username: ")
password_utente = input("Password? ")

if (username_utente == username) and (password_utente == password):
    pin_utente = input("PIN: ")
    if pin_utente == pin:
        print("Accesso Consentito!")
    else:
        print("Errore, pin errato")
        print("Hai esaurito i tentativi a disposizione!")

else:
    print("Errore accesso non consentito!")