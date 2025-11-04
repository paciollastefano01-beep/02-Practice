eta = int(input("Quanti anni hai? "))
autorizzazione = input("Hai l'autorizzazione dei genitori? (si/no): ")
abbonamento = input("Hai l'abbonamento valido? (si/no): ")
certificato_medico = input("Hai certificato medico? (si/no): ")

autorizzazione_ok = autorizzazione.strip().lower() == "si"
abbonamento_ok = abbonamento.strip().lower() == "si"
certificato_ok = certificato_medico.strip().lower() == "si"

requisito_eta_ok = (eta >= 18) or (eta >= 16 and autorizzazione_ok)
accesso_ok = requisito_eta_ok and abbonamento_ok and certificato_ok

motivo = ""
if eta < 16:
    motivo = "Età minima 16 anni"
if motivo == "" and (eta >= 16 and eta < 18) and (not autorizzazione_ok):
    motivo = "Serve autorizzazione genitori"
if motivo == "" and (not abbonamento_ok):
    motivo = "Abbonamento non valido"
if motivo == "" and (not certificato_ok):
    motivo = "Certificato medico non valido"

if accesso_ok:
    print("Accesso Consentito!")
    print("Motivo: tutti i requisiti soddisfatti")
else:
    print(f"Accesso Negato! Motivo: {motivo}")