"""
El Historial de Navegación (def y Class)

Objetivo: Crear una clase llamada Buscador que guarde las páginas web que visita un usuario.

Instrucciones:Define la clase Buscador.En el __init__, 
inicializa una lista vacía en self.historial.

Crea un método llamado visitar_pagina(self, url) que use .append() para guardar la URL.
"""

class Buscador:
    def __init__(self):
        self.historial:list[str] = []
        
    def visitar_pagina(self, url:str):
        self.historial.append(url)

mi_navegador = Buscador()
mi_navegador.visitar_pagina("google.com")
mi_navegador.visitar_pagina("github.com")
print(mi_navegador.historial) 