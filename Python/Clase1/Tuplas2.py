# Recorremos los elementos de una Tupla
cocina = ("cuchara", "cuchillo", "tenedor")

for cocinar in cocina: # Print esta usando \n para saltos de lineas
    print(cocinar, end=" ") # Usamos end= para eliminar los saltos de lineas

cocinaLista = list(cocina)
cocinaLista[0] = "plato"
cocina = tuple(cocinaLista)
print("\n",cocina)

#Eliminamos la Tupla
del cocina
print(cocina)
