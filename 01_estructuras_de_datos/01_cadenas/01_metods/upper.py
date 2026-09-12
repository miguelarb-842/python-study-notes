"""
    La funcion (method) upper() 

    hace que toda cadena de texto pase a mayusculas

    Funcionamiento:
    
        variable:str.upper()
    
        -   si la variable contiene numeros(int) y 
            caracteres especiales
            no se veran afectaron y retoraran igual
        
        -   si otiginalemte estaban en minusculas 
            permaneceran en maysuculas

"""


cadena1:str = "TEXTO"
cadena2:str = "123124"
cadena3:str = "$%$%((()))"
cadena4:str = "HolAAaaa123..."


print(cadena1.upper())
print(cadena3.upper())
print(cadena2.upper())