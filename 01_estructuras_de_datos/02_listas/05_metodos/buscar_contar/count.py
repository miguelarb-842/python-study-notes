"""
    El método .count() recorre la lista completa elemento por elemento Compara 
    cada posición mediante igualdad (==) con el valor que le pasamos.
    
    Cuenta cuántas veces se repite un elemento con el mismo contenido en la lista y retorna la cantidad
    Si el valor no se encuentra en ningún lado, devuelve 0
    Si se llama vacío sin argumentos, lanzará un TypeError
    Al comparar colecciones (como listas anidadas), evalúa el contenido exacto 
    
    por ejemplo, [] no es igual a, ni el entero 2 es igual a la lista.
"""

numeros:list[int] = [1,2,3,4,5,[],[2]]
print(numeros.count(1))
print(numeros.count(2))
print(numeros.count([]))
print(numeros.count([2]))