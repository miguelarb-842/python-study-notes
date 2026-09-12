"""
.split(separador=None, maxsplit=-1)

    metodo ESPECIAL: a diferencia de todos los
    anteriores, este devuelve una LISTA (no un
    string)
    
    divide el string en partes, cortando cada
    vez que encuentra el "separador", y las
    devuelve como elementos de una lista
    
    si NO se pasa separador (se deja vacio):
        separa por CUALQUIER espacio en blanco
        (espacios, tabs, saltos de linea), y
        ademas ignora espacios de mas al 
        principio/final/medio automaticamente
    
    si SI se pasa un separador especifico
    (ej: ","):
        separa exactamente por ese caracter,
        SIN ignorar espacios extra ni valores
        vacios entre separadores repetidos
    
    "maxsplit" (opcional) limita la cantidad
    de cortes, de izquierda a derecha
    
"""

texto: str = "Hola que tal, todo bien"

print(texto.split())              # sin separador: corta por espacios
print(texto.split(","))           # con separador ",": corta ahi especificamente

texto_con_vacios: str = "a,b,,c"
print(texto_con_vacios.split(","))   # ojo: el "" entre comas SI se cuenta como elemento

texto_guiones: str = "a-b-c"
print(texto_guiones.split("-", 1))   # maxsplit=1: solo corta la primera vez