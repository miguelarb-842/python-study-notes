"""
El Gestor de Tareas Prorizadas (Class con append e insert)

Objetivo: Usar append para tareas normales e insert 
para tareas urgentes que deben ir al principio de la lista.Instrucciones:

En el __init__, inicializa self.tareas = [].

En agregar_tarea_normal, usa .append() para mandarla al final.
En agregar_tarea_urgente, usa .insert() para meterla en el índice 0 (al inicio del Heap).
"""

class GestorTareas:
    def __init__(self):
        self.tareas:list[str] = []

    def agregar_tarea_normal(self, tarea: str):
        self.tareas.append(tarea)

    def agregar_tarea_urgente(self, tarea: str):
        self.tareas.insert(0,tarea)

mis_tareas = GestorTareas()
mis_tareas.agregar_tarea_normal("Lavar los platos")
mis_tareas.agregar_tarea_normal("Estudiar Python")
mis_tareas.agregar_tarea_urgente("¡Apagar la estufa!")

print(mis_tareas.tareas)

