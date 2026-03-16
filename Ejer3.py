# Crea un programa que solicite al usuario un número y muestre su tabla de multiplicar
# del 1 al 10 utilizando un bucle for

number = int(input("Ingrese un numero: "))

for n in range(10):
    print(f"{number} x {n+1} = {(n+1)* number}")