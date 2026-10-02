"""
La concatenación es la combinación de dos o más listas mediante el operador +, 
creando una nueva instancia de lista. La nueva variable contiene una referencia 
al nuevo objeto creado en memoria. Las listas originales no son modificadas.

Al concocatenar las listas estas no se ordenan simplemete se añaden tal cual como estan y 
el resultado se asigna a una variable que contiene una referencia al nuevo objeto lista.

Tambien se puden hacer reacionaciones con el operador += 
que guarda la referncia al mismo objeto.

"""

lista_num1:list[int] = [0,1,2,3,4,5]
lista_num2:list[int] = [2,3,4,5,8,1]
suma_de_listas = lista_num1 + lista_num2
print(suma_de_listas)

lista_alt:list[int | str | float | bool] = ["hola",67,False,12.3]
b = lista_num1 + lista_alt
print(b)