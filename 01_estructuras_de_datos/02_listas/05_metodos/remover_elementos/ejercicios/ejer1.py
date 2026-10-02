""" eliminar_valor(lista: list[int], valor: int) -> list[int] — 
    que elimine el valor sin mutar la lista original (devuelve una nueva). 
    Comprueba con id() que la de salida es otro objeto.
"""

def eliminar_valor(lista: list[int] = None, valor: int = None)->list[int] | None:
    
    if lista is None:
        print("No se agrego una lista")
        return None
    
    if valor is None:
        print("No se agrego un valor a eliminar")
        return None
    
    modlist:list[int] = []
    encontrado: bool = False
    
    for val in lista:
        if val == valor and not encontrado:
            encontrado = True
            continue
        
        modlist.append(val)
        
    if not encontrado:
        print("No se hallo el valor")

    return modlist


lista:list[int] = [0,1,2,3,4,5]
nueva_lista = eliminar_valor(lista,0)
print(lista)
print(nueva_lista)
print(id(lista))
print(id(nueva_lista))
  