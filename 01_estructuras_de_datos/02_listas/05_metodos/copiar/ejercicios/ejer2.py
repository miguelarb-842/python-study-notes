"""
Copiando listas de objetos

Usando tu clase Usuario:

Antes de correrlo, responde: 

¿el append de un usuario nuevo afecta a usuarios_originales? 
¿Y el cambio de edad en usuarios_copia[0]? 

Explica por qué usando lo que sabes de Stack/Heap y apuntadores
no solo digas "sí" o "no", justifica con la referencia.
"""

class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def __eq__(self, otro):
        if not isinstance(otro, Usuario):
            return False
        return self.nombre == otro.nombre and self.edad == otro.edad


# Definimos unos usuarios
usuario1 = Usuario("Miguel", 17)
usuario2 = Usuario("Conny", 16)

usuarios_originales: list[Usuario] = [usuario1, usuario2]
usuarios_copia = usuarios_originales.copy()

# usuarios_copia[0] y usuarios_originales[0] son dos apuntadores DISTINTOS,
# pero ambos apuntan al MISMO objeto Usuario en el Heap (el .copy() solo
# duplicó los apuntadores, no los objetos). Por eso, modificar .edad desde
# cualquiera de los dos caminos afecta al mismo objeto compartido.
usuarios_copia[0].edad = 99

# Aquí en cambio sí se agrega un apuntador NUEVO al arreglo propio de
# usuarios_copia. Cada lista tiene su propio arreglo de apuntadores
# (aunque al inicio compartían los mismos objetos), así que este .append()
# solo extiende el arreglo de usuarios_copia, sin tocar el de usuarios_originales.
usuarios_copia.append(Usuario("Nuevo", 20))

"""
¿El append de un usuario nuevo afecta a usuarios_originales?
NO, porque cada lista tiene su propio arreglo de apuntadores. El .copy()
copió el contenido de ese arreglo (los apuntadores), pero usuarios_copia
y usuarios_originales siguen siendo dos listas independientes. Agregar un
elemento solo extiende el arreglo de la lista sobre la que se llama .append().

¿Y el cambio de edad en usuarios_copia[0]?
SÍ afecta a usuarios_originales, porque usuarios_copia[0] y
usuarios_originales[0] apuntan al MISMO objeto Usuario en el Heap
(no se copió el objeto, solo el apuntador hacia él). Modificar .edad
entra directamente al objeto compartido, así que el cambio se ve
desde cualquiera de los dos apuntadores.
"""

print(usuarios_originales)
print(usuarios_copia)
usuarios_originales.append(Usuario("kaka", 17))
print(usuarios_originales[2].nombre)
print(usuarios_copia[2].nombre)