"""
Filtrado de Números Pares (def aislada)

Objetivo: Practicar cómo poblar una lista vacía dentro de una función usando un bucle.
Instrucciones: Crea una función llamada filtrar_pares(lista_numeros) que reciba una lista de enteros, 
identifique los pares y los agregue con .append() a una nueva lista interna para luego retornarla.

"""


def filtrar_pares(lista_numeros: list[int]) -> list[int]:
    lista_pares = [] 
    num:int
    
    for num in lista_numeros:
        if num % 2 == 0:
            lista_pares.append(num)
    
    return lista_pares

# Prueba tu código:
numeros = [1, 2, 3, 4, 5, 6]
resultado = filtrar_pares(numeros)
print(resultado) 