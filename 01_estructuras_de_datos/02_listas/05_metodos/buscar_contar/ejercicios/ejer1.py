"""

    Inventario simple

    Tienes esta lista de códigos de productos (algunos repetidos):

    python
    codigos: list[str] = ["A1", "B2", "A1", "C3", "A1", "D4", "B2"]

    Escribe una función resumen_stock(lista: list[str]) -> None que:

    Imprima cuántos elementos tiene la lista en total (len).
    Imprima cuántas veces aparece "A1" (.count()).
    Verifique con in si "Z9" está en la lista y con not in si "D4" NO está, imprimiendo un mensaje para cada caso.
    Use .index() para encontrar la posición de la primera aparición de "B2"

"""


def resumen_stock(lista: list[str]) -> None:
    
    while True:
        print(f"""
              
            \nLa cantidad de elementos en la lista es: {len(lista)}
              
            (para cualquier caso escriba salir para salir del programa)
              """)
        buscar = str(input("Ingrese un valor para a buscar en la lista: ")).upper()
        
        if buscar is "SALIR":
            print("saliendo del programa")
            return None
        
        print(lista.count(buscar))
        
        if buscar in lista:
            print("si esta en la lista")
            continue
        print("no esta en la lista")
        
        try:
            print(f"su primera posicion es {buscar}")
            
        except ValueError:
            print("No esta en la lista")

codigos: list[str] = ["A1", "B2", "A1", "C3", "A1", "D4", "B2"]

resumen_stock(codigos)