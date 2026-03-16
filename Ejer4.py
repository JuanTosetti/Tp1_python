# Crea un programa que dado un número N ingresado por el usuario, imprima los
# números del 1 al N pero saltee los múltiplos de 5. Nota: utilizá la sentencia continue donde haga falta

number = int(input("Ingresa un numero: "))

for i in range(1,number):
    if (i % 5 != 0):
        print(i)