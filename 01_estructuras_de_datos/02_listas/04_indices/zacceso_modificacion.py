"""Se hace con el operador [] seguido del índice 
    aca lo que se hace es crear una instacia de valor 
    y se asigna el valor en esa posicion de esa lista"""
    
frutas = ["manzana", "banana", "cereza", "durazno"]
nombre = frutas[1]
print(frutas)
print(frutas[0])
print(nombre)

"""Para reaginar el valor en una posicion especifica 
solo se reaccina a esa pocicion un nuevo valor """

frutas[0] = "kiwi"
print(frutas)
print(frutas[0])