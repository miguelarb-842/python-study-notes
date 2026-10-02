"""

    El método .pop() modifica la lista original directamente en el Heap,
    eliminando la referencia que la lista tiene hacia ese objeto 
    (y si ningún otro elemento apunta a él, el Garbage Collector liberará el valor de la memoria). 
    
    A diferencia de .remove(), .pop() no espera un valor, sino un índice de tipo entero (int) que representa 
    la posición en el Stack de la lista. Además, a diferencia de .remove(), .pop() 
    tiene la cualidad de retornar (devolver) el objeto eliminado, 
    permitiéndote guardarlo en otra variable si lo necesitas.
    
    Si se ingresa un tipo de dato que no sea un entero (como un str o un dict), 
    Python lanzará un TypeError porque el método exige un objeto con __index__ (por eso int y bool sirven, float no).
    
    Si se ingresa la posición es en el arreglo interno de punteros, que vive en el Heap.
    
    sobre lista vacía lanza IndexError aunque no pases argumento
    
    pop() elimina por defecto el último elemento de la lista (índice -1).

"""

numeros:list[int] = [1,2,3,4,5]
eliminado = numeros.pop()
print(eliminado)
print(numeros)