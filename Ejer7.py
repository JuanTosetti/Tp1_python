# Escribe un programa que solicite al usuario una lista de palabras. Luego, construí una
# oración uniendo únicamente las palabras que tengan más de 3 letras, separadas por
# espacios. Las palabras cortas deben ser excluidas del resultado final

palabras = []
oracion = []
for i in range(10):
    palabras.append(input("Ingrese una palabra "))
print(palabras)

for i in palabras:
    if len(i) > 3 :
        oracion.append(i)

resultado = " ".join(oracion)
print(resultado)