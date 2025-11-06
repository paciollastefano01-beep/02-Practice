è_iscritto = (input("Sei iscritto? ")).strip().lower()
ha_certificato = (input("Hai certificato (si/no)? ")).strip().lower()
ha_pagato = (input("Hai pagato (si/no)? ")).strip().lower()
temperatura = float(input("Temperatura? "))

if è_iscritto == "si" and ha_certificato == "si" and ha_pagato == "si" and temperatura >= 36:
    print("Accesso Consentito!")
elif ha_certificato == "no":
    print("Manca il certificato!")
elif è_iscritto == "no":
    print("Non sei iscritto!")
elif ha_pagato == "no":
    print("Non hai pagato!")
elif temperatura < 36:
    print("Temperatura non idonea!")
else:
    print("Input non valido. Rispondi solo con 'si' o 'no' oppure inserisci un numero per la temperatura.")
