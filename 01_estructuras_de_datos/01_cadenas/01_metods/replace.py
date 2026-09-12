"""
.replace(viejo, nuevo, cantidad=-1)

    busca todas las apariciones de "viejo" dentro
    del string y las cambia por "nuevo"
    
    NO modifica el string original (los strings
    son inmutables) - devuelve un string NUEVO
    
    el tercer parametro (opcional) limita cuantas
    apariciones reemplazar, de izquierda a derecha
    si no se pasa, reemplaza TODAS
    
    es sensible a mayusculas/minusculas
    
"""

texto: str = "Hola que tal, que dia tan lindo"

print(texto.replace("que", "QUE"))         # reemplaza TODAS
print(texto.replace("que", "QUE", 1))      # reemplaza solo la primera
print(texto)                                # el original sigue intacto