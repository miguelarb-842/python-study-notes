"""
    
    El método .copy() realiza una COPIA SUPERFICIAL (shallow copy) de la lista:
    
    - Genera una nueva lista en el Heap con un ID de memoria único.
    - Duplica los apuntadores de los elementos de la lista original hacia la nueva.
    - Para datos inmutables (int, str), actúan de forma independiente al modificarse.
    - Para datos mutables anidados (listas, dicts), ambas listas comparten el mismo 
    apuntador en el Heap, por lo que modificar el interior de uno alterará al otro.
    
"""

original = [1, 2, [99]]
copia = original.copy()

# 1. Modificar un entero no afecta a la otra lista
copia[0] = 500
print(original)  # [1, 2, [99]]   no cambió
print(copia)     # [500, 2, [99]]  Cambió de forma independiente

# 2. Modificar la sublista AFECTA A AMBAS
copia[2].append(100)
print(original)  # [1, 2, [99, 100]] tambien se modifica
print(copia)     # [500, 2, [99, 100]