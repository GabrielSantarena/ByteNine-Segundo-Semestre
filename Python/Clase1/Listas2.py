nombres = ["Agustin", "Gabriel", "Lili", "Ariel"]
print(nombres)

print(nombres[0:2]) #Solo muestra el indice 0 y 1, pero no el indice 2

# ir del inicio de la lista al indice (sin incluirlo)
print(nombres[ :3]) # Indices a mostrar 0, 1 y 2

#Desde el indice indicado hasta el final
print(nombres[1: ])

#Modificamos un valor
nombres[2] = "Marcos"
nombres[0] = "Agus"
print(nombres)

#Iterar una lista

for nombre in nombres: # nombre es singular, la lista es prural
    print(nombre)
else:
    print("Se acabaron los elementos de la lista")