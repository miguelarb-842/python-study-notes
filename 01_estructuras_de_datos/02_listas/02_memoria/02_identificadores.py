"""
Por defecto python retorna el valor de id de 
direccion de memoria de cualquier objeto en decimal 
con las funciones hex y bin podemos retornar un valor disntinto.

"""


lista:list[int] = [0,1,2,3,4,5,6,7]

print(hex(id(lista)))
print(bin(id(lista)))


"""De esa mamera de convierte el valor decimal de la lista un hexa-decimal o binario"""

def mostar_direccion(objeto:object = None):
    
    if objeto is None:
        print("Se requiere ingresar un argumento a la funcion")
        return
    
    direccion_de_memoria = id(objeto)
    
    return f"""
            Decimal: {direccion_de_memoria}
            Hexadecimal: {hex(direccion_de_memoria)}
            Binario: {bin(direccion_de_memoria)}
        """

print(mostar_direccion(lista))
    