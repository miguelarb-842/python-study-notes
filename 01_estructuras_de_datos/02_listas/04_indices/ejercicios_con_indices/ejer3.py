"""

Intercambio de posiciones

Dada numeros = [10, 20, 30, 40, 50], escribí código 
que intercambie el primer y el último elemento usando 
índices (positivos o negativos), sin usar ningún método 
de lista todavía (los vemos en la próxima sección).

"""


numeros = [10, 20, 30, 40, 50]

def intercabiar_primer_utimo(lista:list)->None:
    
    n = len(lista) - 1
    
    primer_num = lista[0]
    ultumo_num = lista[n]
    
    lista[0] = ultumo_num
    lista[n] = primer_num


print(numeros)
intercabiar_primer_utimo(numeros)
print(numeros)

