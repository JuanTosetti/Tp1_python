#  Modifica el ejercicio 4 para que, en lugar de imprimir los números, genere dos listas:
# una con los múltiplos de 5 y otra con el resto de los números. Imprimí ambas listas al
# finalizar.

number = int(input("Ingresa un numero: "))
multiplos_cinco = []
otros_numeros = []

for i in range(1, number + 1): 
    if i % 5 == 0:
        multiplos_cinco.append(i)
    else:
    otros_numeros.append(i)

print("IMPRESION DE LISTAS ------------")
print(f"Multiplos de 5: {multiplos_cinco}")
print(f"Otros numeros {otros_numeros}")