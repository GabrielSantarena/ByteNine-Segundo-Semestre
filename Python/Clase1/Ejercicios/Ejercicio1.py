#Ercicio 1: Iterar un rango de 0 a 10 e imprimir números divisibles entre 3
#Ejemplo de ejecución: 0,3,6,9

Lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in Lista:
    if num % 3 == 0:
        print(num)
