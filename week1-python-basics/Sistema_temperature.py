print("\n=== ANALIZZATORE DI TEMPERATURA ===")

temperatura = float(input("Temperatura in °C: "))

if temperatura >= 35:
    print("🔥 MOLTO CALDO! Stai all'ombra!")
elif temperatura >= 25:
    print("☀️ Caldo, Vestiti Leggero!")
elif temperatura >= 15:
    print("🌤️  Mite, Temperatura Gradevole!")
elif temperatura >= 5:
    print("🧥 Fresco, Porta Giacca!")
else:
    print("🧊 Gelo, Rischio Ghiaccio")

print("Analisi Completata.")
