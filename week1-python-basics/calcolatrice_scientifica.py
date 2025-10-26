# 🧮 CALCOLATRICE SCIENTIFICA - Progetto Giorno 2

print("=" * 50)
print("🧮 CALCOLATRICE SCIENTIFICA")
print("=" * 50)

# Input numeri
print("\nInserisci due numeri:")
num1 = float(input("Primo numero: "))
num2 = float(input("Secondo numero: "))

# Menu operazioni
print("\n" + "=" * 50)
print("OPERAZIONI DISPONIBILI:")
print("=" * 50)
print("1. Addizione (+)")
print("2. Sottrazione (-)")
print("3. Moltiplicazione (×)")
print("4. Divisione (÷)")
print("5. Divisione intera (//)")
print("6. Modulo (resto, %)")
print("7. Potenza (**)")
print("=" * 50)

scelta = input("\nScegli operazione (1-7): ")

# Calcoli
print("\n" + "=" * 50)
print("RISULTATO:")
print("=" * 50)

if scelta == "1":
    risultato = num1 + num2
    print(f"{num1} + {num2} = {risultato}")

elif scelta == "2":
    risultato = num1 - num2
    print(f"{num1} - {num2} = {risultato}")

elif scelta == "3":
    risultato = num1 * num2
    print(f"{num1} × {num2} = {risultato}")

elif scelta == "4":
    if num2 != 0:
        risultato = num1 / num2
        print(f"{num1} ÷ {num2} = {risultato:.4f}")
    else:
        print("❌ ERRORE: Impossibile dividere per zero!")

elif scelta == "5":
    if num2 != 0:
        risultato = num1 // num2
        print(f"{num1} // {num2} = {risultato}")
    else:
        print("❌ ERRORE: Impossibile dividere per zero!")

elif scelta == "6":
    if num2 != 0:
        risultato = num1 % num2
        print(f"{num1} % {num2} = {risultato}")
    else:
        print("❌ ERRORE: Impossibile dividere per zero!")

elif scelta == "7":
    risultato = num1**num2
    print(f"{num1} ** {num2} = {risultato}")

else:
    print("❌ ERRORE: Scelta non valida!")

print("=" * 50)
print("✅ Calcolo completato!")
print("=" * 50)
