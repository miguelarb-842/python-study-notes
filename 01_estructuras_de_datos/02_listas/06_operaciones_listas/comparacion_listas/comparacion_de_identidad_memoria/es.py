"""

El operador is no mira el contenido. 

Evalúa si ambas variables apuntan a la misma instancia exacta en el Heap 
es decir, si tienen el mismo id

Este devolvera False cuando no esten apuntando al mismo espacio y true cuando si
"""

a = [1,2,3]
b = [1,2,3]
c = a
d = b

print(hex(id(a)))
print(hex(id(b)))
print(hex(id(c)))
print(hex(id(d)))

print(a is a)
print(a is b)
print(a is c)
print(a is d)
print(b is b)
print(d is b)

