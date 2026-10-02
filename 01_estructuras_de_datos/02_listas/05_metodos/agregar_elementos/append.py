""" El metodo append() agrega un nuevo elemento al final de la lista. 
    El metodo como tal retorna None lo que hace en si no 
    modifica ni crea una nueva memoria en el heap que vive la lista
    el solo agrega una nueva direccion de memoria de stack que vive en la 
    lista osea el heap.
    
"""
    
lista:list[int] = [0,1,2,3,4,5,6,7,8,9]
lista.append(10)
print(lista)