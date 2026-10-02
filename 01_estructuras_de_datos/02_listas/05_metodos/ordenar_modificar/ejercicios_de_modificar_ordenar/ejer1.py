"""
Dada la siguiente lista de precios, ordenala de menor a mayor 
usando sort(). Luego, sin crear una lista nueva, ordenala 
de mayor a menor.


precios: list[float] = [45.50, 12.99, 89.00, 3.25, 67.10]

# TODO: ordena ascendente
# TODO: imprime
# TODO: ordena descendente (reverse)
# TODO: imprime

"""

precios: list[float] = [45.50, 12.99, 89.00, 3.25, 67.10]

precios.sort()
print(precios)

precios.sort(reverse=True)
print(precios)