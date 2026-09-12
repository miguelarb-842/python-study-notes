"""
En python los indices de una lista son un referencia numerica 
asignada a un elemento empezando desde 0 no desde 1. En esa posicion 
es el indice, veamoslo con un ejemplo anterior.
"""


frutas = ["manzana", "banana", "cereza", "durazno"]

"""Los indices positivos cuentan de derecha a izquierda"""

elemento1 = frutas[0]
elemento2 = frutas[1]
elemento3 = frutas[2]
elemento4 = frutas[3]

print(elemento1,elemento2,elemento3,elemento4)

"""Los indeces negativos cuentan desde el final de la lista hacia la 
izuqierda empezando desde -1"""

elemento_nega1 = frutas[-1]
elemento_nega2 = frutas[-2]
elemento_nega3 = frutas[-3]
elemento_nega4 = frutas[0]

print(elemento_nega1,elemento_nega2,elemento_nega3,elemento_nega4)