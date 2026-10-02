"""

El operador * se conoce como repetición este operador funciona de la siguiente forma: 

    lista * n 
    
Siendo n un número entero es decir de tipo int 

- Si este número entero es negativo se genera una lista vacía ya que Python interpreta que debe realizar 0 
repeticiones mismo caso ocurre si se utiliza 0 como multiplicador 

- Si se ingresa un valor incorrecto, se generará un TypeError 

La lista que se genera es un nuevo objeto. La variable que recibe el resultado contiene una 
referencia hacia ese nuevo objeto

Se puede realizar una reasignación utilizando el operador *=: 
    
    lista *= n 
    
En este caso, la lista se modifica para repetir sus elementos n veces

Tambien duplicaciones de un elemto de la lista 

    lista[i] *= n

"""

lista_num1:list[int] = [0,1,2,3,4,[5,6]]
print(lista_num1)

duplicacion = lista_num1 * 2
print(duplicacion)

lista_num1 *= 2
print(lista_num1)

lista_num1[5] *= 5
print(lista_num1)