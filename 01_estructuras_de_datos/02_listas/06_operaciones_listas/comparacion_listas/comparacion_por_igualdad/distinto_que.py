"""
Si que la misma logica de su contra parte de igualdad ("==") este cambia el lugar de la comparacion 
y devuelve un booleano

El resultado será True si ambas listas NO contienen los mismos elementos
en la misma cantidad y en el mismo orden. 

Si algún elemento es diferente devolvera true

si las listas tienen diferente cantidad de elementos o si el orden es diferente
el resultado será True. La comparación se realiza elemento por
"""

lista1:list[int] = [1,2,3,4]
lista2:list[int] = [0,1,2,3,4]
lista3:list[int] = [1,3,4,2]
lista4:list[int] = [1,2,3,4]

print(lista1 != lista4)
print(lista2 != lista1)
print(lista1 != lista3)
print(lista1 != lista1)
