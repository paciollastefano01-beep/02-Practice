nome = input("Come ti chiami? ")
cognome = input("Qual'è il tuo cognome? ")
citta = input("Da quale città vieni? ")
soprannome = input("Qual'è il tuo soprannome? ")

print(nome, cognome, "di", citta)  # stampa con più argomenti
print(f"{nome} {cognome} di {citta}")  # con f-string controllo io esattamente gli spazi

print(
    f"{nome} '{soprannome}' {cognome} di {citta}"
)  # Aggiunta soprannome tra virgolette a testo

