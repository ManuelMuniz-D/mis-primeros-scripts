"""Demostración de if, elif, else con rangos de edad.

Python evalúa las condiciones de arriba abajo y ejecuta solo el primer
bloque verdadero.
Cuando encuentra una condición verdadera, ejecuta su bloque y se detiene.
elif = “si no, pero…”.
else = “si nada anterior se cumplió”.
"""

edad = int(input("¿Cuántos años tienes?\n"))

if edad >= 18:
    print("Eres mayor de edad.")
elif edad >= 13:
    print("Erea adolescente.")
else:
    print("Eres menor de esdad.")
