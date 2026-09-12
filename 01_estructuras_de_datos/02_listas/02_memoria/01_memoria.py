"""
En Python, absolutamente todos los objetos 
(listas, strings, ints, diccionarios, todo) se 
crean y viven en el heap.Esto es diferente a 
lenguajes como C, donde una variable local simple 
puede vivir en el stack.

"""
Lista:list[ str | int ] = ["hola","Miguel",17]
print(id(Lista))          # dirección en memoria (como entero decimal)

lista:list[int] = [0,1,2,3,4,5,6,7]

def saber_direc(objeto:object = None):

    if objeto == None:
        print("Se espera un arguemnto de entrada")
        return
    
    print(id(objeto))
    return

"""
Como podemos observar devuelve una direccion de memoria en decimal (123456789)
"""