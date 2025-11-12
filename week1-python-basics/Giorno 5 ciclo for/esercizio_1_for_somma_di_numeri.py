n = int(input("Quanti numeri vuoi sommare? "))

if n == 0:
    print("Non hai inserito numeri da sommare!")
else:
    somma = 0

    for i in range(n):
        numero = float(input(f"Numero {i + 1}: "))

        somma = somma + numero
        print(f"Somma parziale: {somma:.2f}")

    media = somma / n
    print(f"\nLa somma dei numeri che hai scelto è: {somma:.2f}")
    print(f"La media dei numeri scelti è: {media:.2f}")
