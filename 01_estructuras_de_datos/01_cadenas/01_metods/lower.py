"""
    La funcion (method) lower() 

    hace que toda cadena de texto pase a minusculas

    Funcionamiento:
    
        variable:str.lower()
    
        -   si la variable contiene numeros(int) y 
            caracteres especiales
            no se veran afectaron y retoraran igual
        
        -   si otiginalemte estaban en minusculas 
            permaneceran en minusculas

"""


cadena1:str = "TEXTO"
cadena2:str = "123124"
cadena3:str = "$%$%((()))"
cadena4:str = "HolAAaaa123..."


print(cadena1.lower())
print(cadena3.lower())
print(cadena2.lower())