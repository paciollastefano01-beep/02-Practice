print("=" * 50)
print("🎮 GIOCO: INDOVINA IL NUMERO!")
print("=" * 50)
print("Ho pensato a un numero fra 1 e 10.")
print("Hai un tentativo per indovinare")
print()

numero_segreto = 7
tentativo = int(input("Quale Numero ho pensato? "))

if tentativo == numero_segreto:
    print("\n🎉 INCREDIBILE! HAI INDOVINATO!🎉")
    print(f"Il numero era proprio {numero_segreto}!")
    print("Sei un Campione! 🏆")
elif tentativo < numero_segreto:
    print(f"\n📉 Troppo Basso!")
    print(f"Il numero era {numero_segreto}")
    print("Ritenta, Sarai più fortunato! 🍀")
elif tentativo > numero_segreto:
    print(f"\n📈 Troppo Alto!")
    print(f"Il numero era {numero_segreto}")
    print("Ritenta, sarai più fortunato! 🍀")

print("\n" + "=" * 50)
print("Grazie per aver giocato")
print("=" * 50)
