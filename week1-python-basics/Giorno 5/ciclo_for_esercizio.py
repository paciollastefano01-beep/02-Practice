print(list(range(2, 7)))
print(list(range(1, 10, 2)))
for numero in range(5):
    print(numero)

for i in range(3):
    print(f"Giro {i}")

# Consolidamento teoria
print("ESPERIMENTO 1: range base")
for i in range(4):
    print(f"i vale: {i}")

print("\nESPERIMENTO 2: range con start")
for n in range(3, 7):
    print(f"n vale: {n}")

print("\nESPERIMENTO 3: range con step")
for x in range(0, 10, 3):
    print(f"x vale: {x}")

# for loops avanzati
parola = "ciao"
for lettera in parola:
    print(lettera)
