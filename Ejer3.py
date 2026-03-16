# Crea un programa que solicite al usuario un número y muestre su tabla de multiplicar
# del 1 al 10 utilizando un bucle for

number = int(input("Ingrese un numero: "))

for n in range(1,11):
    print(f"{number} x {n} = {(n)* number}")