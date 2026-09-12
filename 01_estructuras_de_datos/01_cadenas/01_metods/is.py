"""
.isnumeric()

    verifica si la cadena contiene SOLO digitos
    numericos, devuelve True o False
    
    aunque el valor este declarado como str,
    recorre caracter por caracter para verificar
    que TODOS sean numeros
    
    detalles importantes (casos que fallan):
    
        "-5".isnumeric()    -> False (el signo
                                "-" no es un digito)
        "12.5".isnumeric()  -> False (el punto
                                tampoco es un digito)
    
    por eso: si necesitas validar negativos o
    decimales, .isnumeric() NO alcanza, hay que
    combinarlo con otra logica (o usar try/except
    con int()/float() directamente)
    
.isalpha()

    verifica que la cadena sea solamente texto y
    caracteres, sin ningun valor numerico
    
    solo acepta letras de la A-Z (incluye tildes
    y letras acentuadas en Python 3)
    
    los espacios y simbolos como #"!., NO cuentan
    como letras, asi que una cadena con espacios
    (ej: "Hola Mundo") da False
    
"""

print("123".isnumeric())     # True
print("-5".isnumeric())      # False
print("12.5".isnumeric())    # False

print("Hola".isalpha())      # True
print("Hola Mundo".isalpha())  # False, tiene un espacio