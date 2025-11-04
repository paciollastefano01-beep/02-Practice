print("=== SISTEMA LOGIN ===")

username = input("Username: ")
password = input("Password: ")

# uso if/else
if username == "admin" and password == "1234":
    print(f"✅ Benvenuto {username}!")
else:
    print("❌ Credenziali errate")


colore = input("Che colore è il semaforo? ").lower()

if colore == "verde":
    print("✅ Puoi passare!")
elif colore == "giallo":
    print("⚠️  Rallenta, sta per diventare rosso")
elif colore == "rosso":
    print("🛑 FERMATI!")
else:
    print("❓ Colore non valido")


# sistema di valutazione

print("=== SISTEMA VOTI ===")
voto = int(input("Inserisci il voto (0-100): "))

if voto >= 90:
    giudizio = "Eccellente! 🌟"
    lettera = "A"
elif voto >= 80:
    giudizio = "Ottimo! 👏"
    lettera = "B"
elif voto >= 70:
    giudizio = "Buono 👍"
    lettera = "C"
elif voto >= 60:
    giudizio = "Sufficiente ✓"
    lettera = "D"
else:
    giudizio = "Insufficiente 📚"
    lettera = "F"


print(f"Voto: {voto}/100")
print(f"Grado: {lettera}")
print(f"Giudizio: {giudizio}")
