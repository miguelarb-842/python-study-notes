"""
.index(subcadena, inicio=0, fin=len(str))

    funciona IGUAL que .find(): busca la primera
    aparicion de "subcadena" y devuelve su indice
    
    la UNICA diferencia con .find():
    
        si NO encuentra la subcadena, .index()
        LANZA UN ERROR (ValueError), en vez de
        devolver -1
    
    por eso hay que tener cuidado al usarlo:
    si no estas seguro de que la subcadena existe,
    conviene envolverlo en un try/except, o usar
    .find() en su lugar
    
    es sensible a mayusculas/minusculas
    (igual que .find())
    
"""

texto: str = "Hola que tal"

print(texto.index("que"))      # encuentra "que", devuelve su indice (5)

print(texto.index("xyz"))      # ValueError: substring not found