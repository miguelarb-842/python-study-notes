"""
    'in' es un operador de membresía (pertenencia) que actúa como un filtro lógico 
    devuelviendo un flag (True o False). Opera bajo las mismas reglas de comparación 
    que .index() al buscar la referencia del objeto en el Heap usando el apuntador 
    que viene desde el Stack.
    
    - Si la condición de igualdad (__eq__) se cumple, devuelve True; de lo contrario, False
    - Al devolver un booleano es muy común combinarlo con estructuras de control
    
    El not in es un operador unico de membresia not solamente cambia o invierte la logica 
    o la flag que de devuelve el operador.
    
"""

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

if nuevo_miguel in lista_usuarios:
    print("si")

lista:list[int] = [1,2,3,4]

if 2 in lista:
    print("Aguacate")
    
if 10 not in lista:
    print("Pera")

print (0 in lista)