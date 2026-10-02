"""

El operador is not funciona al igual que su contraparte is

Evalúa si ambas variables apuntan a la misma instancia exacta en el Heap 
es decir, si tienen el mismo id al ser esto verdad de volvera false

Este devolvera True cuando no esten apuntando al mismo espacio y true cuando si
"""

a = [1,2,3]
b = [1,2,3]
c = a
d = b

print(hex(id(a)))
print(hex(id(b)))
print(hex(id(c)))
print(hex(id(d)))

print(a is not a)
print(a is not b)
print(a is not c)
print(a is not d)
print(b is not b)
print(d is not b)
