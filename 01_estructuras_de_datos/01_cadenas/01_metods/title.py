"""
.title()

    convierte la primera letra de CADA PALABRA 
    a mayuscula, y el resto de cada palabra a 
    minuscula
    
    diferencia con .capitalize():
    
        .capitalize() solo pone en mayuscula la
        primera letra de TODO el string, y el
        resto queda en minuscula
        
        .title() lo hace palabra por palabra
    
    una "palabra" para .title() es cualquier 
    secuencia separada por espacios (o algunos
    otros simbolos)
    
"""

texto: str = "hola que tal estas"

print(texto.title())         # cada palabra con mayuscula inicial
print(texto.capitalize())    # solo la primera letra de todo el string