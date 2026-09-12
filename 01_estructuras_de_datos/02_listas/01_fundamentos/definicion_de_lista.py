"""
List es un metodo comun que se ocupa para generar una lista 
Las listas son un recurso de organizacion para guardar multiples datos dentro de una vairble que es un tipo lista. Las listas en Python son estructuras de datos ordenadas y mutables que permiten almacenar múltiples valores de cualquier tipo en una sola variable.

Las listas en python son mutables es decir que se pueden editar sus valores originales dentro de una funcion, python hace un **Call by reference** que es una llamada (puntero) de referencia de memorias
en donde enves de crear una insidencia/objeto nuevo lo que se hace en una modificacion especifica a ese objeto que vive en ese espacio de memoria asignado.

En Python, absolutamente todos los objetos (listas, strings, ints, diccionarios, todo) se 
crean y viven en el heap.Esto es diferente a lenguajes como C, donde una variable local simple puede vivir en el stack.
"""

Lista:list[ str | int ] = list(["hola","Miguel",17])

"""
No es la forma mas recomendable de hacerlo pero si una practica
el los () son opcionales los [] obligariotios y que el metodo list
es una clase lista en si genera una instancia de una lista.
"""

Lista:list[ str | int ] = ["hola","Miguel",17]
"""
    Forma correcta
"""



