print("TABELLINA DEL 2")
print("-" * 15)  # trucco: stampa 15 trattini

for i in range(1, 11):  # da 1 a 10
    risultato = 2 * i  # calcola 2 * i
    print(f"2 x {i} = {risultato}")

tabellina = input("Quale tabellina vuoi? ")
print(f"\nTABELLINA DEL {tabellina}")
print("-" * 15)
for i in range(1, 11):
    risultato = int(tabellina) * i
    print(f"{tabellina} x {i} = {risultato}")
