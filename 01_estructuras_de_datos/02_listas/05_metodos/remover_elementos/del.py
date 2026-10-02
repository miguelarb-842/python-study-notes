"""

    A diferencia de .remove(), .pop() o .clear(), del no es un método, 
    sino una palabra clave (keyword) o instrucción nativa de Python. 
    
    Su función principal no es borrar objetos directamente de la memoria, 
    sino al objeto del namespace (frame local o globals()), 
    y también opera sobre índices, slices, claves de dict y atributos.
    
    del borra datos enteros de referncias a ese objeto mas que todo no 
    elimina el objeto como tal si no la referncia de ese dato al heap de donde se este ocupando
    en caso que esta no tenga mas referencias ella queda huerfana y Garbage Collector en CPython 
    se liberan de inmediato al llegar el refcount a 0. El GC generacional solo limpia ciclos de referencias.
    
    Si intentas usar la variable después de borrarla, Python lanzará un NameError.

"""

nombre = "julia"

datos = [nombre, "ana", "pedro"]
del datos[0]
print(datos)
print(nombre)

numeros:list[int] = [1,2,3,4,5]

del numeros[1:3]
print(numeros)

del numeros
"""una vez realisado esta accion ya no se puede volver acceder a esa varibale"""

