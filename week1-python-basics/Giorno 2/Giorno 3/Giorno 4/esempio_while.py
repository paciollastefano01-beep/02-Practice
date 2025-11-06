# esempio: countdown

secondi = 5

print("Preparati...")

while secondi > 0:
    print(f"{secondi} secondi al via!")
    secondi = secondi - 1  # Diminuisce invece di aumentare

print("🚀 PARTENZA!")

#primo esempio in assoluto while

numero = 1

while numero <= 3:
    print(numero)
    numero = numero + 1

print("Fine")

x = 10
while x >= 7:
    print(f"x vale {x}")
    x = x - 1
print("Finito!")

# VOGLIAMO solo "si" o "no", nient'altro!
risposta = ""  # Inizializziamo con stringa vuota

while risposta != "si" and risposta != "no":
    risposta = input("Vuoi continuare? (si/no): ").strip().lower()

    if risposta != "si" and risposta != "no":
        print("❌ Per favore, rispondi solo 'si' o 'no'")

print(f"Hai risposto: {risposta}")

# Metodo 1: Inizializzare con valore impossibile
numero = 0

while numero < 1 or numero > 10:
    numero = int(input("Inserisci numero da 1 a 10: "))

    if numero < 1:
        print("❌ Troppo piccolo!")
    elif numero > 10:
        print("❌ Troppo grande!")
# Se è nel range, non stampa nulla e esce

print(f"✅ Numero valido: {numero}")