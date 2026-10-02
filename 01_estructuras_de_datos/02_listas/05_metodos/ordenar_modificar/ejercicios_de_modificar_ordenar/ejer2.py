"""
Tenes una lista de nombres de estudiantes con longitudes distintas.
Ordena la lista usando key= para que quede ordenada por la 
CANTIDAD DE LETRAS de cada nombre, de menor a mayor.


Despues invertila para que quede de mayor a menor cantidad de letras,
pero sin volver a llamar sort() con reverse=True 
(usa reverse() sobre el resultado ya ordenado).

nombres: list[str] = ["Ana", "Alejandro", "Luis", "Valentina", "Eduardo"]

# TODO: ordena por longitud usando key=len
# TODO: imprime
# TODO: invierte el orden con reverse()
# TODO: imprime

"""



nombres: list[str] = ["Ana", "Alejandro", "Luis", "Valentina", "Eduardo"]
nombres.sort(key= lambda x:len(x))
print(nombres)
nombres.reverse()
print(nombres)
