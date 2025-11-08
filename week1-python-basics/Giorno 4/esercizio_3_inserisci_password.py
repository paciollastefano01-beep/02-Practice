#  ESERCIZIO 3: PASSWORD SEMPLICE
password_corretta = "1234"
tentativo = ""

while tentativo != password_corretta:
    tentativo = input("Password? ").strip()
    if tentativo != password_corretta:
        print("Sbagliata!")

print("Password Corretta")
print("Accesso Consentito!")

