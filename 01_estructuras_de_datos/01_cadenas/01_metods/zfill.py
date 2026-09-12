"""
.zfill(ancho)

    rellena el string con CEROS a la izquierda
    hasta completar el ancho pedido
    
    parecido a .rjust(ancho, "0"), pero con un
    comportamiento especial para signos negativos
    
    si el string ya es igual o mas largo que el
    ancho pedido, lo devuelve sin cambios
    
    detalle especial con negativos:
    
        el signo "-" se mantiene AL PRINCIPIO,
        y los ceros se insertan DESPUES del signo,
        no antes (a diferencia de .rjust() que
        pondria los ceros antes del signo)
    
"""

print("7".zfill(3))       # "007"
print("42".zfill(5))      # "00042"
print("-7".zfill(4))      # "-007" (el signo se mantiene al frente)
print("7".zfill(1))       # "7" (ya cumple el ancho, sin cambios)