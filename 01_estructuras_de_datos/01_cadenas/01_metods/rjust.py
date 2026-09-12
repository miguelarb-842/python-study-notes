"""
.rjust(ancho, caracter_relleno='')

    alinea el texto pegado a la derecha dentro
    de un ancho determinado, agregando el relleno
    solo del lado izquierdo
    
    el primer parametro es obligatorio (el ancho)
    el segundo parametro es opcional (el caracter 
    de relleno, si no se pasa nada usa espacios)
    
    si el ancho pedido es menor o igual al largo 
    del texto, devuelve el texto sin cambios
    
    es el opuesto de .ljust()
    
"""

texto: str = "Hola"

resultado = texto.rjust(20)
print(resultado)

resultado_con_relleno = texto.rjust(20, "-")
print(resultado_con_relleno)