"""
.find(subcadena, inicio=0, fin=len(str))

    busca la PRIMERA aparicion de "subcadena" 
    dentro del string
    
    devuelve el INDICE (posicion) donde empieza 
    la coincidencia
    
    si NO encuentra la subcadena, devuelve -1
    (no lanza error, a diferencia de .index())
    
    los parametros "inicio" y "fin" son opcionales,
    limitan el rango de busqueda dentro del string
    
    es sensible a mayusculas/minusculas
    
"""

texto: str = "Hola que tal"

print(texto.find("que"))       # encuentra "que", devuelve su indice
print(texto.find("QUE"))       # no encuentra (mayusculas distintas), devuelve -1
print(texto.find("z"))         # no existe en el texto, devuelve -1
print(texto.find("a", 5))      # busca "a" mostrando solo desde el indice 5 en adelante