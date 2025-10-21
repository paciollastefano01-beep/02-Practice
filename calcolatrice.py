def somma(a, b):
    return a + b


def sottrai(a, b):
    return a - b


def moltiplica(a, b):
    return a * b


def dividi(a, b):
    if b != 0:
        return a / b
    else:
        return "Errore: divisione per zero!"


# Test
print("Calcolatrice Python 🧮")
x = 10
y = 5

print(f"{x} + {y} = {somma(x, y)}")
print(f"{x} - {y} = {sottrai(x, y)}")
print(f"{x} × {y} = {moltiplica(x, y)}")
print(f"{x} ÷ {y} = {dividi(x, y)}")
