"""
    En Python, una lista heterogénea es aquella que 
    contiene elementos de diferentes tipos de datos 
    (como enteros, cadenas de texto, booleanos, 
    flotantes e incluso otras listas) dentro de
    una misma estructura.

"""

usuario:list[ int | str | bool ] = [1, "Carlos", 28, True] 
producto1:list[ int | str | float] = [3, "Papa", 43.50 ]

nombres:list[dict[str:any]] = [
    
    {"Producto":"Papa", "Precio":43.50, "Stock":3},
    {"Producto":"cacao", "Precio":20, "Stock":3},
    {"Producto":"leche", "Precio":39.99, "Stock":3},
    {"Producto":"queso", "Precio":80, "Stock":3},
   
]