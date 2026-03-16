# Escribe un programa que solicite al usuario una cantidad de segundos y muestre
# cuántas horas, minutos y segundos equivalen. Por ejemplo, 3661 segundos son 1
# hora, 1 minuto y 1 segundo

segundos_ingresados = int(input("Ingresa una cantidad de segundos: "))

seg = segundos_ingresados
minutos = int(seg / 60)
seg = segundos_ingresados % 60
hora = int(minutos / 60)
minutos = minutos % 60

print(f"{hora} horas {minutos} minutos y {seg} segundos")