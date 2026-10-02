"""

    Predecir antes de correr

    Sin ejecutar el código, escribe en un comentario qué esperas que imprima cada línea,
    y luego corre para verificar:

    matriz: list[list[int]] = [[1, 2], [3, 4], [5, 6]]
    copia_matriz = matriz.copy()

    copia_matriz[0] = [99, 99]
    copia_matriz[1][0] = 500

    print(matriz)
    print(copia_matriz)

    ¿Por qué la primera línea (copia_matriz[0] = [...]) no afecta a matriz, 
    pero la segunda (copia_matriz[1][0] = ...) sí?


"""

matriz: list[list[int]] = [[1, 2], [3, 4], [5, 6]]
copia_matriz = matriz.copy()


copia_matriz[0] = [99, 99] # ESTO NO AFECTA EN NADA PORQUE SE ESTA AÑADIENDO EN LA COPIA OSEA UNA REFERECNIA
# ESPECIFICAMENTE A ESA MATRIZ 

copia_matriz[1][0] = 500 # MIENTRAS QUE ACA SE ESTA MODIFICANDO UN ELEMENTO DE QUE VIVE EN UN HEAP
# LO QUE PASA QUE SON UN ELEMENTO EN COMUN A MODIFICARSE ACA SE MODIFICA EN OTRO LADO 
# ES COMO UNA VENTA SI SE AÑADE UN MONTO EN CAJA TAMBIEN SE MODIFICA EN LA FACTURACION AL FINAL DEL DIA 
# PORQUE COMPARTEN EN LA MISMA TIENDA OSEA EN ESTE CASO LA REFERENCIA 

# PENSEMOS EN EL CASO ANTERIOR EN LA COPIA ES UNA NUEVA REFERENCIA QUE SE ESTA AÑADIENDO QUE NO COMPARTEN 
# EN EL STACK SI MODIFICAMOS EL ELEMNTO 99,99 NO DEBE DE MUTAR EN LA ORIGINAL PORQUE LA ORGINAL 
# NO COMPARTE ESA REFERENCIA DE DATO


print(matriz) #  [[1, 2], [500, 4], [5, 6]]
print(copia_matriz) # [[99,99], [500, 4], [5, 6]]
