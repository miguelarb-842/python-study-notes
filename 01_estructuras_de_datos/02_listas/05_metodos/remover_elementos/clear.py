"""
    El método .clear() modifica la lista original directamente en el Heap, 
    eliminando todas las referencias que la lista tiene hacia sus elementos/objetos de forma simultánea, 
    sin importar el tipo de dato que almacene (ya sean primitivos o estructuras complejas).
    
    A diferencia de 
    .remove() o .pop(), este método no requiere ningún argumento (no recibe valores ni índices) 
    y no genera errores de rango o tipo, ya que su única función es romper el vínculo entre la lista 
    y todos los objetos a los que apuntaba.Tras ejecutar .clear(), la estructura de la lista permanece 
    intacta en el Heap (mantiene su misma dirección de memoria o id()), pero queda completamente vacía. 
    
    Los objetos que estaban dentro serán destruidos, CPython se liberan de inmediato al llegar 
    el refcount a 0. El GC generacional solo limpia ciclos de referencias.

"""

numeros:list[int] = [1,2,3,4,5]
numeros.clear()
print(numeros)