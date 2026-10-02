"""
En una lista trabajamos con elementos cada parte de la 
lista es un elementoal ocupar len() cuenta la cantidad 
de elementos que hay en la List sin importar el tipo.

La lista guarda apuntadores (referencias) a objetos que viven en el Heap 
Python obtiene directamente el conteo de estas referencias

"""


Lista:list[ str | int ] = ["hola","Miguel",17]
cantidad_elemt = len(Lista)
print(cantidad_elemt)