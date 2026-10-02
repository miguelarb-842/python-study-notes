"""
    El extend() es un metodo para extender una lista con elemento iterable que significa no
    acepta un metodo solo aislado tiene que ser una dict un conjunto una lista 
    pero de manera iterable. Si se le ingresa un dato no iterable mandara un TypeError

"""

lista_a:list[int] = [1, 2]
# lista_a.extend(1) error por que no es iteralble

b:{int} = {3,4}
lista_a.extend(b)

print(lista_a)

"al contrario lo que pasara con sus hermanos"

lista_a.append(b)
lista_a.insert(2,b)


