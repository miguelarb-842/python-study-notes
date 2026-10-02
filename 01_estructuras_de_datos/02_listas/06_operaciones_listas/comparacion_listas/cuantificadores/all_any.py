"""

All()
Este pregunta que si todos los elementos de una lista cumplen una condición o están en otra lista
el hace la comparacion uno por uno y retorna un booleano

termina siendo verdad cuando comple todo en caso contrado es falso

all(x in [b] for x in a) 

Any()

La función any() comprueba si al menos uno de los elementos 
de un iterable cumple una determinada condición.


se hace con una forma muy general 

termina siendo verdad cuando al menos uno cumple si acaso ninguno cumple entonces es falso
"""

a = [1,1]
b = 1

print(all(x in [b] for x in a))

permisos_usuario = ["leer", "escribir"]
permisos_requeridos = ["leer", "escribir", "eliminar"]

tiene_todo = all(p in permisos_usuario for p in permisos_requeridos)
print(tiene_todo)

tiene_almenos_uno = any(p in permisos_usuario for p in permisos_requeridos)
print(tiene_almenos_uno)


