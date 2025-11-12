# for loop con liste 2 modi
# Modo 1: iterare sui valori

frutti = ["mela", "pera", "uva"]

for frutto in frutti:
    print(f"Mi piace: {frutto}")

#   MODO 2: Iterare sugli INDICI:


frutti = ["mela", "pera", "uva"]

for i in range(len(frutti)):
    print(f"Posizione {i}: {frutti[i]}")
