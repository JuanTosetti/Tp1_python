# Escribe un programa que simule una caja registradora: el usuario ingresa precios de
# productos de a uno. Cuando ingresa 0, el programa se detiene y muestra el total
# acumulado. Nota: utilizá la sentencia break cuando haga falta

total = int(input("Ingrese el monto a cargar "))
suma = 0
while True:
    if total == 0:
        break
    suma += total
    total = int(input("Ingrese el monto a cargar "))

print(f"El total es {suma}")