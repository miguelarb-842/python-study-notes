"""
.index() es un método de las listas en Python. Por defecto recorre la
lista buscando el valor que queremos y devuelve el índice (la posición)
de la primera coincidencia que encuentra, el recibe hasta 3 argumentos:
 
    value: es obligatorio es el elemento a buscar
    start: es opcional es la posición donde inicia la búsqueda
    stop es opcional Posición donde se detiene (no incluida)

 - Si el valor no está en la lista el lanzará un ValueError
 - start como stop admiten números negativos (cuentan desde el final)
 - La búsqueda siempre se realiza de izquierda a derecha
 
  OJO: Si no defines el método especial de igualdad __eq__ 
  en tu clase el index() comparará las direcciones de 
  memoria reales en el Heap. Es decir solo encontrará el 
  objeto exacto si pasas la misma referencia de variable 
  pero fallará si creas un objeto nuevo con los mismos datos internos
"""

numeros:list[int] = [1,2,3,4,5,1]
nom:str = ["Jose","Miguel"]
a = numeros.index(1,-1)
#b = numeros(2,3,6) # lanza error porque en ese rango no esta el numero
c = numeros.index(2,0,5)
d = numeros.index(1,-6,5) # siempre incia de izquierda a derecha a izquerda
print(a,c)

def buscar_por_id(lista:list = None , valor:any = None)-> int | None:
    
    if lista is None:
        print("No se ingreso una lista")
        return None
    
    if valor is None:
        print("No se ingreso un valor para buscar")
    
class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def __eq__(self, otro):
        if not isinstance(otro, Usuario):
            return False
        return self.nombre == otro.nombre and self.edad == otro.edad
    


lista_usuarios = [Usuario("Miguel", 25)]
nuevo_miguel = Usuario("Miguel", 25)

# print(lista_usuarios.index(nuevo_miguel)) fallara al por que no es la misma misma direccion
#print(lista_usuarios.index(Usuario("Miguel", 25))) aca igualmente no es la misma dirrecon 

"""El bug se soluciona al añadir __eq__ en la clase y funcionara"""

