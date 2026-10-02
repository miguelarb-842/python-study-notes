"""
Tenes una lista de diccionarios que representa un inventario.
Cada diccionario tiene "producto", "precio" y "stock".

1. Ordena la lista por "precio" de menor a mayor.
2. Ordena la lista por "stock" de mayor a menor.
3. Ordena la lista alfabeticamente por "producto", 
   pero ignorando mayusculas/minusculas 
   (pista: la key puede transformar el string antes de comparar).
   
   
inventario: list[dict[str, object]] = [
    {"producto": "mouse", "precio": 15.99, "stock": 30},
    {"producto": "Teclado", "precio": 45.00, "stock": 12},
    {"producto": "monitor", "precio": 199.99, "stock": 5},
    {"producto": "Cable HDMI", "precio": 8.50, "stock": 50},
]

# TODO: ordena por precio ascendente
# TODO: imprime

# TODO: ordena por stock descendente
# TODO: imprime

# TODO: ordena por producto, ignorando mayus/minus
# TODO: imprime

Imprime la lista completa despues de cada ordenamiento para 
verificar el resultado.
"""

inventario: list[dict[str, object]] = [
    {"producto": "mouse", "precio": 15.99, "stock": 30},
    {"producto": "Teclado", "precio": 45.00, "stock": 12},
    {"producto": "monitor", "precio": 199.99, "stock": 5},
    {"producto": "Cable HDMI", "precio": 8.50, "stock": 50},
]


inventario.sort(key= lambda x: x["precio"])
print("\n\n")
for producto in inventario:
    print (f"{producto['producto']}, precio: {producto['precio']}, stock: {producto['stock']}")

inventario.sort(key= lambda x:x["stock"],reverse= True)
print("\n\n")
for producto in inventario:
    print (f"{producto['producto']}, precio: {producto['precio']}, stock: {producto['stock']}")
    
    
inventario.sort(key= lambda x: x["producto"].lower())
print("\n\n")
for producto in inventario:
    print (f"{producto['producto']}, precio: {producto['precio']}, stock: {producto['stock']}")
    