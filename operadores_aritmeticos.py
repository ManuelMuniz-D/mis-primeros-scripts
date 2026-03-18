"""Operadores aritméticos y comparaciones básicas.

Este script solicita dos números al usuario, realiza operaciones
aritméticas básicas (suma, resta, multiplicación) y las muestra,
además de comparar cuál número es mayor.

Ejemplo:
    Número A: 10
    Número B: 5
    Suma: 15
    Resta: 5
    Multiplicación: 50
    ¿A es mayor que B? True
"""




a = int(input("Número A: "))
b = int(input("Número B: "))

print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("¿A es mayor que B?", a > b)
