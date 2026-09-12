"""
.strip()

    elimina espacios en blanco (y saltos de linea)
    del INICIO y del FINAL del string
    NO afecta los espacios que estan en el medio
    
    tambien puede recibir un caracter especifico
    a eliminar, en vez de espacios
    
    variantes:
    
        .lstrip()  -> solo elimina del lado 
                      izquierdo (inicio)
        .rstrip()  -> solo elimina del lado 
                      derecho (final)
        .strip()   -> elimina de ambos lados
    
    NO modifica el original, devuelve un string
    nuevo (igual que todos los metodos de cadena)
    
"""

texto: str = "   Hola que tal   "

print(f"[{texto.strip()}]")     # elimina espacios de ambos lados
print(f"[{texto.lstrip()}]")    # elimina solo de la izquierda
print(f"[{texto.rstrip()}]")    # elimina solo de la derecha

texto2: str = "###Hola###"
print(texto2.strip("#"))        # elimina el caracter "#" de ambos lados