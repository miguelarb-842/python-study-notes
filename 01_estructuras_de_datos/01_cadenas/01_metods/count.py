"""
.count(subcadena, inicio=0, fin=len(str))

    cuenta cuantas veces aparece "subcadena"
    dentro del string, SIN solapar coincidencias
    
    si no encuentra ninguna, devuelve 0
    (nunca lanza error, a diferencia de .index())
    
    es sensible a mayusculas/minusculas
    
    los parametros "inicio" y "fin" son opcionales,
    limitan el rango de busqueda (igual que en
    .find())
    
"""

texto: str = "la casa de la vaca"

print(texto.count("a"))       # cuenta todas las "a" del texto
print(texto.count("la"))      # cuenta cuantas veces aparece "la" completo
print(texto.count("xyz"))     # no existe, devuelve 0
print(texto.count("a", 5))    # cuenta "a" solo desde el indice 5 en adelante