"""

Crea una funcion en la que podamos recorrer 
un objeto especificios de una lista y en caso 
que no este imprimir que no se econtro 

"""

def hallar_elemento(lista:list,indice:int)-> object | None:
    
    try:
        elemento = lista[indice]
        print(elemento)
        return elemento
        
    except IndexError:
        print("No se pudo encontrar ese elemnto en la lista")

frutas = ["manzana", "banana", "cereza", "durazno"]

hallar_elemento(frutas,2)
hallar_elemento(frutas,23)