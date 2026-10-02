"""
    El metodo remove funciona con el valor que se quiere el liminar se elimina de forma derecta en el stock
    y modifica a la lista original en el heap. El metodo remove toma el valor directo del la instancia del self 
    al objeto que se este ocupando si el objeto toma una intancia de objeto de dato primitivo int este espera que sea un int
    igualmente si es un str o algun otro tipo de dato. 
    
    El remove funciona con un call object by Reference para ayar la referncia a ese valor asu ves borrar el valor y su referencia
    del stock no una referencia por lo que cuando tengamos un listas de referncias que viven el heap como dict o un ArrayList
    se tiene que pasar los datos especificos para borrarlos.
    
    Cuando se ingresa un dato fuera de rango (elemnto que o valor que no se encuentra en la lista) manda un error de valor 
    ya que no es un valor que se encuentre en la lista.
    
    Al retornar None este no devuelve ningun valor
"""

numeros:list[int] = [1,2,3,4,5]
print(numeros)

nombres:list[str] = ["Adrian","Carlos","Ramira","Delmis","Rogelio"]
nombres.remove("Adrian")
print(nombres)

datos:list[dict[str:any]] = [{"nombre":"julia"},{"nombre":"ana"}]
datos.remove({"nombre":"julia"})
print(datos)

matriz:list[list[int]] = [
    [1,0],
    [0,1]
    ]

matriz.remove([1,0])
print(matriz)