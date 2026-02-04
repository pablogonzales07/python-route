
try:
    numero = 10/0
except ZeroDivisionError:
    print("No se puede dividir po 0")

try:
    print(x)
except NameError:
    print("Variable indefinida")
finally:
    print("Esto se ejecuta si o si")