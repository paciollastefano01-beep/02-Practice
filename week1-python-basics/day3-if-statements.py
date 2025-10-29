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
