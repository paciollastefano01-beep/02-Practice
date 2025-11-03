anno_corrente = 2025
mese_corrente = 11

anno_di_nascita = int(
    input("In quale anno sei nato? ")
)  # chiedo anno e converto in intero già
mese_di_nascita = int(input("In che mese sei nato? (1/12) "))

eta = anno_corrente - anno_di_nascita
if mese_corrente < mese_di_nascita:
    eta = eta - 1

print(f"Hai {eta} anni")
