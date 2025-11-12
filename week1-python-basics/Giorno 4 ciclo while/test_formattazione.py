# CODICE VOLUTAMENTE MAL FORMATTATO
trovato=False#senza spazi
posti=0
while posti<3 and not trovato:
 dove=input("Dove guardo? (cassetto/armadio/tavolo): ")
 if dove=="cassetto":
  print("Trovato!")
  trovato=True
 else:
     print("Non c'è")
     posti=posti+1
if trovato:print("Posso usare l'oggetto")
else:print("Non l'ho trovato da nessuna parte")
