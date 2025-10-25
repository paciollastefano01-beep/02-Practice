# 📝 Python Cheat Sheet - Giorno 1

> Appunti veloci per ricordare sintassi Python base

---

## 🎯 Variabili

### Assegnazione base

```
python


# Creare variabile

x = 5

nome = "Mario"

prezzo = 19.99

attivo = True
```

## 📊 Tipi di Dati

### I 4 tipi fondamentali

| Tipo         | Nome Python | Esempio         | Quando usare           |
| ------------ | ----------- | --------------- | ---------------------- |
| **Intero**   | `int`       | `42`, `-10`     | Contare, età, quantità |
| **Decimale** | `float`     | `3.14`, `19.99` | Prezzi, temperature    |
| **Testo**    | `str`       | `"Ciao"`        | Nomi, messaggi         |
| **Booleano** | `bool`      | `True`, `False` | Vero/Falso             |

### Scoprire tipo variabile

```undefined


x = 42
print(type(x))  # Output: <class 'int'>
```

## 🖨️ Stampare (Print)

### Modi base

```python

# Stampare testo
print("Ciao mondo!")

# Stampare variabile
nome = "Mario"
print(nome)

```

### F-strings (MIGLIORE!)

```python
nome = "Mario"
eta = 25

# F-string
print(f"Mi chiamo {nome} e ho {eta} anni")
```

## ⌨️ Input (Chiedere dati)

### Input base

```python
# Chiede e salva in variabile
nome = input("Come ti chiami? ")
print(nome)
```

### Convertire input in numero

```python
# Stringa → Intero
eta = int(input("Età: "))

# Stringa → Decimale
prezzo = float(input("Prezzo: "))
```

## 🔄 Conversioni Tipo

### Tabella conversioni

```python
# Stringa → Intero
int("42")        # Risultato: 42

# Stringa → Decimale
float("3.14")    # Risultato: 3.14

# Numero → Stringa
str(42)          # Risultato: "42"

# Decimale → Intero (tronca!)
int(3.99)        # Risultato: 3
```

## 🚨 Errori Comuni

### ❌ ERRORE 1: Sommare stringa + numero

```python
# SBAGLIATO
eta = input("Età: ")  # eta è STRINGA
print(eta + 5)  # ❌ ERRORE!

# CORRETTO
eta = int(input("Età: "))
print(eta + 5)  # ✅ Funziona!
```

## 📌 Template Pronti

### Template: Chiedere nome ed età

```python
nome = input("Nome: ")
eta = int(input("Età: "))
print(f"Ciao {nome}, hai {eta} anni!")
```

## 🔗 Link Utili

- [Python Docs](https://docs.python.org/3/)
- [W3Schools Python](https://www.w3schools.com/python/)
- [Real Python](https://realpython.com/)

---

_Ultimo aggiornamento: Giorno 1_
_Prossimo: Operatori matematici (Giorno 2)_
