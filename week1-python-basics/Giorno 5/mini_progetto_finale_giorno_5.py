# mini progetto : analizzatore di testo

print("=== ANALIZZATORE DI TESTO ===")
print("-" * 30)

testo = input("Inserisci il testo da analizzare:\n ").strip().lower()

caratteri_totali = 0
spazi = 0
lettere = 0
vocali = 0
consonanti = 0
a = 0
e = 0
i = 0
o = 0
u = 0

for carattere in testo:
    caratteri_totali = caratteri_totali + 1
    if carattere == " ":
        spazi = spazi + 1
    elif carattere >= "a" and carattere <= "z":
        lettere = lettere + 1
        if (
            carattere == "a"
            or carattere == "e"
            or carattere == "i"
            or carattere == "o"
            or carattere == "u"
        ):
            vocali = vocali + 1
            if carattere == "a":
                a = a + 1
            elif carattere == "e":
                e = e + 1
            elif carattere == "i":
                i = i + 1
            elif carattere == "o":
                o = o + 1
            elif carattere == "u":
                u = u + 1

        else:
            consonanti = consonanti + 1

campione = a
vincitrice = "a"
if e > campione:
    campione = e
    vincitrice = "e"
if i > campione:
    campione = i
    vincitrice = "i"
if o > campione:
    campione = o
    vincitrice = "o"
if u > campione:
    campione = u
    vincitrice = "u"


print("\n=== RISULTATI ===")
print("-" * 30)
print(f"La tua frase ha {caratteri_totali} caratteri totali")
print(f"La tua frase ha {spazi} spazi")
print(f"Nel testo sono presenti {lettere} lettere")
print(f"Nel testo sono presenti {vocali} vocali")
print(f"Nel testo sono presenti {consonanti} consonanti")
print(f"la vocale più frequente è la {vincitrice} ed è apparsa {campione} volte ")
print("-" * 30)
