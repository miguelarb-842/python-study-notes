"""
Buscador de usuarios con manejo de errores

Usando tu clase Usuario (con __eq__ ya implementado), escribe una función:

python
def buscar_usuario(lista: list[Usuario], objetivo: Usuario) -> int | None:
    ...

que:

Use in primero para verificar si objetivo está en la lista.
Si está, use .index() para obtener y retornar su posición.
Si no está, imprima un mensaje y retorne None 
(evita que se lance el ValueError, atrápalo o valida antes con in).

Como extra, agrega una segunda función que cuente cuántos usuarios en la lista 
tienen el mismo nombre que objetivo (pista: no puedes usar .count() directamente 
aquí porque compara el objeto completo — tendrás que recorrer la lista a mano o con una comprensión de listas).
"""

class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def __eq__(self, otro):
        if not isinstance(otro, Usuario):
            return False
        return self.nombre == otro.nombre and self.edad == otro.edad


usuario1 = Usuario("Miguel",17)
usuario2 = Usuario("Marbelly",18)
usuario3 = Usuario("Conny",16)
usuario4 = Usuario("Allan",17)
usuario5 = Usuario("Marcia",17)
usuario6 = Usuario("Miguel",17)
usuario7 = Usuario("Miguel",17)

lista_de_usuarios:list[Usuario] = [usuario1,usuario2,usuario3,usuario5,usuario6,usuario7]

def buscar_usuario(lista: list[Usuario], objetivo: Usuario) -> int | None:
    
    if objetivo in lista:
        print(lista.index(objetivo))
        return lista.index(objetivo)
    
    print("No esta en la lista")
    return None

def repetios(lista: list[Usuario], objetivo: Usuario) -> int:
    
    
    contador:int = 0
    for usuario in lista:
        if usuario.nombre == objetivo.nombre:
            contador += 1
            continue

    print(f"La cantidad de usuarios con el mismo nombre es {contador}")
    return contador
    
buscar_usuario(lista_de_usuarios,usuario2)
buscar_usuario(lista_de_usuarios,usuario4)
repetios(lista_de_usuarios,usuario1)
        
        
                           
    
