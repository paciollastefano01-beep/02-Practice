# Test finale VS Code Setup
# Verifica: Pylance, Black, Execution


def fibonacci(n):
    """Genera sequenza Fibonacci fino a n numeri"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib


def analizza_numeri(numeri):
    """Analizza lista di numeri"""
    if not numeri:
        return "Lista vuota"

    somma = sum(numeri)
    media = somma / len(numeri)
    massimo = max(numeri)
    minimo = min(numeri)

    return {"somma": somma, "media": media, "massimo": massimo, "minimo": minimo}


# Test
print("=" * 50)
print("TEST FINALE VS CODE SETUP")
print("=" * 50)

# Fibonacci
print("\n1. Test Fibonacci:")
fib_seq = fibonacci(10)
print(f"Fibonacci(10): {fib_seq}")

# Analisi
print("\n2. Test Analisi Numeri:")
risultato = analizza_numeri(fib_seq)
for chiave, valore in risultato.items():
    print(f"  {chiave}: {valore}")

# Input utente
print("\n3. Test Input:")
nome = input("Come ti chiami? ")
print(f"Ciao {nome}! Setup VS Code completato! 🎉")

print("\n" + "=" * 50)
print("✅ TUTTI I TEST SUPERATI!")
print("=" * 50)
