# Esercizio di chiedere qualcosa all'utente

risposta = ""
while risposta != "no":
    risposta = input("Vuoi continuare? (si/no): ").strip().lower()

if risposta == "no":
    print("Arrivederci!")
