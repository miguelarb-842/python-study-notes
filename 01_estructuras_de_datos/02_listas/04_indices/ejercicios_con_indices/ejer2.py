"""
Validación de rango manual

Escribí una función esta_en_rango(lista, indice) -> bool que 
devuelva True o False según si ese índice es válido para esa lista, 
sin usar try/except — usando la fórmula del rango (-n a n - 1).

"""

def esta_en_rango(lista:list, indice:int)->bool:
    
    n = len(lista) 
    return -n <= indice <= n - 1


frutas = ["manzana", "banana", "cereza", "durazno"]
print(esta_en_rango(frutas,-5))