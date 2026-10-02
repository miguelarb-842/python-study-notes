"""

Crea una clase Producto con atributos codigo: str y precio: float, 
sin definir __eq__ todavía. 

Crea una lista con 3 instancias de Producto y 
luego un objeto nuevo con los mismos datos que uno de los que ya está en la lista.

Primero intenta usar in para ver si ese objeto nuevo "está" en la lista. 
¿Qué resultado da y por qué (piensa en Stack/Heap)?

Ahora agrega el método __eq__ a la clase (comparando codigo y precio) y vuelve a correr la misma prueba. 
¿Cambió el resultado?

Intenta usar .index() con ese mismo objeto nuevo antes y 
después de tener __eq__. 
¿Qué pasa si no está en la lista — qué excepción salta?

"""

class Producto:
    def __init__(self,precio:float,codigo:str):
        self.precio:int = precio
        self.codigo:str = codigo
    
    def __eq__(self, value):
        
        if not isinstance(value,Producto):
            return float
        return self.precio == value.precio and self.codigo == value.codigo
    
    
producto1 = Producto(12,"A1")
producto2 = Producto(8.6,"A2")
producto3 = Producto(9.99,"A3")

lista_prodcuto:list[Producto] = [producto1,producto2,producto3]
nuevo_producto = Producto(12,"A1")

print(nuevo_producto in lista_prodcuto) # comparará las direcciones de memoria reales en el Heap
print(lista_prodcuto.index(nuevo_producto)) # da un ValueError el elemento no esta en la lista

