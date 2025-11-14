# ESERCIZIO 3: TROVA IL MAGGIORE
lista_numeri = []

print("===================")
print("Inserisci 5 numeri")
print("===================")

for i in range(5):
    numeri_utente = int(input(f"\nInserisci numero {i + 1}: "))
    lista_numeri.append(numeri_utente)

massimo = lista_numeri[0]
for numero_presente in lista_numeri:
    if numero_presente > massimo:
        massimo = numero_presente

print(f"\nIl valore più grande che hai inserito è {massimo}")
