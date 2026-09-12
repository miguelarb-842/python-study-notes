"""
.startswith(cadena)

    verifica si el string EMPIEZA con la cadena
    dada, devuelve True o False
    
.endswith(cadena)

    verifica si el string TERMINA con la cadena
    dada, devuelve True o False
    
    ambos son sensibles a mayusculas/minusculas
    
    ambos pueden recibir una TUPLA de varias
    opciones en vez de un solo string - devuelve
    True si coincide con CUALQUIERA de ellas
    
"""

archivo: str = "documento.pdf"

print(archivo.startswith("doc"))     # True
print(archivo.endswith(".pdf"))      # True

print(archivo.endswith((".pdf", ".docx", ".txt")))   # True, coincide con una de la tupla

print(archivo.startswith("Doc"))     # False, sensible a mayusculas