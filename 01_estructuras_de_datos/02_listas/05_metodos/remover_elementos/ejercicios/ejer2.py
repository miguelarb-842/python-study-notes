"""
    eliminar_todas(lista: list[int], valor: int) -> int
    
    elimina todas las ocurrencias (no solo la primera) y devuelve cuántas quitó. Pruébala con [1,2,1,1,3].
"""

def eliminar_todas(lista: list[int] = None, valor: int = None) -> int | None:
    
    if lista is None:
        print("No se agrego una lista")
        return None
    
    if valor is None:
        print("No se agrego un valor a eliminar")
        return None
    
    total_eliminados:int = lista.count(valor)
    
    while valor in lista:
        lista.remove(valor)
        
    print(f"Total de elminados: {total_eliminados}")
    print(lista)
    return total_eliminados

nums = [1,2,1,1,3]
eliminar_todas(nums,1)
        