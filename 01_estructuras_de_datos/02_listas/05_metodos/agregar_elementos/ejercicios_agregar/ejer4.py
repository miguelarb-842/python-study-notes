"""
El Sincronizador de Contactos (Class con extend)

Objetivo: Usar .extend() para fusionar una lista o conjunto entero de nuevos 
contactos dentro de la agenda de la clase de un solo golpe.

Instrucciones: El método importar_contactos recibe un iterable 
(una lista o un set de nombres) y debe desempaquetarlos en el Heap de self.agenda.

"""

class Agenda:
    def __init__(self):
        self.agenda = ["Ana", "Pedro"]

    def importar_contactos(self, nuevos_contactos):
        self.agenda.extend(nuevos_contactos)
        pass

# Prueba tu código:
mi_agenda = Agenda()

# Nuevos contactos que vienen de un conjunto (Set)
nuevos = {"Carlos", "Maria"} 

mi_agenda.importar_contactos(nuevos)
print(mi_agenda.agenda)
