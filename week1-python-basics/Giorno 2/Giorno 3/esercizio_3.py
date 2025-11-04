temperatura = float(input("Quale temperatura? "))

if temperatura < 0:
    print("Ghiacciato ❄️")
elif temperatura <= 10:
    print("Molto freddo 🥶")
elif temperatura <= 20:
    print("Fresco 🌤️")
elif temperatura <= 30:
    print("Piacevole 😊")
elif temperatura <= 40:
    print("Caldo 🌞")
else:
    print("Torrido 🔥")
