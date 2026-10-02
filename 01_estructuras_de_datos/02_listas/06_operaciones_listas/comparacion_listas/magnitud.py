"""

Los comparadores logicos de manginud < > <= >=

Estas comparaciones se realizan de forma lexicográfica
osea python compara los elementos de las listas desde 
el primero hasta encontrar una diferencia que permita determinar el resultado. 

La comparación debe realizarse entre listas
 
Si se intenta comparar una lista directamente con un tipo de dato incompatible
como un int, se generará un TypeError

"""

lista1:list[int] = [1,2,3,4]
lista2:list[int] = [0,1,2,3,4]
lista3:list[int] = [1,3,4,2]
lista4:list[int] = [1,2,3,4]

print(lista1 < lista2)
print(lista1 > lista2)
print(lista1 <= lista4)
print(lista1 > lista3)
