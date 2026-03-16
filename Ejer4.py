# Crea un programa que dado un número N ingresado por el usuario, imprima los
# números del 1 al N pero saltee los múltiplos de 5. Nota: utilizá la sentencia continue donde haga falta

number = int(input("Ingresa un numero: "))

for i in range(1,number + 1):
    if (i % 5 != 0):
        print(i)

for i in range(1, number + 1): #Ahora el rango va air tambien hasta el numero ingresado
    if(i % 5 == 0):
        continue
    print(i)