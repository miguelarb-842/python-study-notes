"""
len(objeto)

    NO es un metodo de cadena (no lleva punto)
    es una funcion incorporada (built-in)
    
    devuelve la cantidad de elementos que tiene
    un objeto:
    
    - en un str: cuenta los caracteres (incluye
      espacios y simbolos)
    - en una list: cuenta los elementos
    - en un dict: cuenta las claves (pares
      clave-valor)
    
"""

texto: str = "Hola que tal"
print(len(texto))          # cuenta caracteres, incluidos espacios

lista: list[str] = ["Hola", "que", "tal"]
print(len(lista))          # cuenta elementos

diccionario: dict = {"nombre": "Miguel", "edad": 20}
print(len(diccionario))    # cuenta claves