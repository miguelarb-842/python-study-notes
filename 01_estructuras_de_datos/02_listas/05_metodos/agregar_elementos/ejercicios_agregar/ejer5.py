def procesar_inventario(
    inventario_base: list, 
    producto_normal: str, 
    producto_top: str, 
    lote_nuevos: list
    ) -> list:
    
    inventario_base.append(producto_normal)
    inventario_base.insert(0,producto_top)
    inventario_base.extend(lote_nuevos)

    return inventario_base


inventario = ["Laptop", "Mouse"]

resultado = procesar_inventario(
    inventario_base=inventario,
    producto_normal="Teclado",
    producto_top="Monitor 4K",
    lote_nuevos=["Pad", "Cables"]
)

print(resultado)