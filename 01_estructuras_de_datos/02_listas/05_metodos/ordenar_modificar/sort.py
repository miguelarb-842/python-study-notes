"""
El metodo sort() ordena la lista de forma ascendente o descendente, esto no genera 
una nueva instancia, modifica el orden del arreglo de referencias en el heap in-place.

Recibe dos argumentos (ambos opcionales, keyword-only):

reverse: por defecto esta en False (orden ascendente), sirve para ordenarla en orden 
descendente si esta en True
key: recibe una funcion que transforma cada elemento antes de compararlo, normalmente 
funciones lambda

Como al ser un metodo y no genera instancia, este retorna None siempre

"""

# ordena la lista de menor a mayor (ascendente por defecto)
lista:list[int] = [8,1,5,2,4,4,6,3]
print(lista)
lista.sort()
print(lista)


# ordena de mayor a menor (descendente)
lista.sort(reverse=True)
print(lista)

# ordenar en base a una key 

frutas:list[str] = ["Manzana", "Banana", "Cereza", "Pera"]

# ordena alfabeticamente (orden lexicografico por defecto)
frutas.sort()
print(frutas)

# oden inverso
frutas.sort(reverse=True)
print(frutas)

# ordena de menor a mayor longitud de string
frutas.sort(reverse=False, key=len)
print(frutas)

frutas.sort(reverse=True, key=len)
print(frutas)


# ordena a partir del segundo elemento de la tupla
estudiantes:list[tuple[str,int]] = [("Ana", 23), ("Luis", 19), ("Pedro", 21)]

estudiantes.sort(key=lambda x: x[1])
print(estudiantes)

estudiantes_dict = [{"nombre":"Julian"},{"nombre":"Ana"},{"nombre":"Vanessa"}]

estudiantes_dict.sort(key=lambda x: len(x["nombre"]))
print(estudiantes_dict)

estudiantes_dict.sort(key=lambda x: x["nombre"])
print(estudiantes_dict)