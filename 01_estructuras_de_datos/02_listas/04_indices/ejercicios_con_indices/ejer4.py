"""

Reto — índice del medio

Dada una lista de longitud impar, escribí una función elemento_medio(lista) 
que devuelva el elemento justo del centro, usando solo índices (sin recorrer con for). 
Pensá cómo calcular ese índice a partir de len(lista)."""

numeros = [10, 20, 30, 40, 50]

def medio(lista:list) -> int | None:
    
    n = len(lista)
    if n % 2 == 0:
        print ("No se puede manejar esa cantidad de numeros")
        return None
    
    indice_medio:int = n // 2
    print(f"el valor medio es: {indice_medio}")
    print(f"El valor medio asignado es {lista[indice_medio]}")
    return indice_medio

medio(numeros)