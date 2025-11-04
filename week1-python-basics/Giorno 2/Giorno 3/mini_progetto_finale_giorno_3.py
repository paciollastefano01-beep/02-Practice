# mini bot che chiede cose e suggerisce soluzioni

stanchezza = input("Sei stanco? (Si/No) ").strip().lower()
fame = input("Hai fame: (Si/No) ").strip().lower()
uscita = input("Vuoi uscire? (Si/No) ").strip().lower()
budget = float(input("Budget a disposizione (£)? "))

if stanchezza == "si" and uscita == "no":
    print("Potresti rilassarti a casa e vederti un bel film")
elif budget >= 20 and fame == "si":
    print("Potresti andare a cena fuori e goderti la serata come si deve!")
elif budget < 20 and uscita == "si" and fame == "no":
    print("Puoi farti una passeggiata e prenderti del tempo per te stesso")
elif stanchezza == "si" and fame == "si" and budget > 20:
    print("Potresti ordinare qualcosa da mangiare su just eat")
elif (fame == "si" or stanchezza == "si") and budget < 20:
    print("Potresti leggerti un bel libro!")
