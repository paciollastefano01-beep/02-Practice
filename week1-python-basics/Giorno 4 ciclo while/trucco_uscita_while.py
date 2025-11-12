# Gioco con uscite multiple
import random  # Per numeri casuali (non preoccuparti dei dettagli)

numero_segreto = random.randint(1, 10)
tentativi = 0
max_tentativi = 5
indovinato = False

while tentativi < max_tentativi:
    guess = input("Indovina (1-10) o 'quit' per uscire: ")

    # Uscita 1: l'utente vuole smettere
    if guess == "quit":
        print("😔 Hai abbandonato!")
        break

    # Convertiamo in numero
    guess = int(guess)
    tentativi = tentativi + 1

    # Uscita 2: ha indovinato
    if guess == numero_segreto:
        print(f"🎉 BRAVO! Era {numero_segreto}!")
        indovinato = True
        break

    # Feedback se non ha indovinato
    if guess < numero_segreto:
        print("📈 Troppo basso!")
    else:
        print("📉 Troppo alto!")

    print(f"Tentativi rimasti: {max_tentativi - tentativi}")

# Dopo il while, vediamo come è uscito
if not indovinato and tentativi >= max_tentativi:
    print(f"😵 Hai perso! Il numero era {numero_segreto}")
