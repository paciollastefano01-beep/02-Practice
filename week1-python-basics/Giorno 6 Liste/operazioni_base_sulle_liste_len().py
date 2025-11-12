# LUNGHEZZA con len():

spesa = ["pane", "latte", "uova"]
lunghezza = len(spesa)
print(f"Ho {lunghezza} prodotti")  # Output: Ho 3 prodotti

# Utile con for!
for i in range(len(spesa)):
    print(f"{i + 1}: {spesa[i]}")
