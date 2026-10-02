"""
    El insert() funciona bajo la misma logica de append busca un self de referencia
    y un objeto a hacer agregado pero aca pasa algo mas, el espera un argumento de 
    indice y su parametro es un index el ubica al objeto en una posicion espesifica.
    
    si en caso que no se lleve a ingresar el argumento esperado el 
    lanzara un TypeError de que espera 2 argumentos y solo se ingreso uno
    si en caso de ingresar un indece mucho mayor el siempre lo pondra al final de la lista.
    y la continuidad sera normal
"""

lista:list[float] = [0,1,2,3,4,5,6,7,8,9]
lista.insert(100,10)
lista.insert(11,11)
lista.insert(12,12)
lista.insert(3,2.578)
print(lista)