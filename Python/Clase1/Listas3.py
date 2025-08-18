nombres = ["Agustin", "Gabriel", "Lili", "Ariel"]
print(nombres)

# Preguntamos cuantos elementos tiene
print(len(nombres)) #Le pasamos como parametro nuestra lista

#Agregamos un elemento
nombres.append("Marcelo")
print(nombres)

#Insertar un elemento en un indice especifico
nombres.insert(1,"Alberto")
print(nombres)
nombres.insert(3, "Debora")
print(nombres)

#Eliminamos un elemento
nombres.remove("Marcelo")
print(nombres)

#Eliminar el ultimo elemento
nombres.pop()
print(nombres)

#Eliminamos un indice especifico
del nombres[2] # del significado delete (eliminar)
print(nombres)

#Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

# Eliminar la lista 
del nombres
print(nombres) #Aqui nos muestra un error