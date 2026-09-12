"""
    La funcion (method) capitalize() 

    hace que la primera letra de la cadena pase a maysuculas

    Funcionamiento:
    
        variable:str.capitalize()
    
        -   si la variable contiene numeros(int) y 
            caracteres especiales
            no se veran afectaron y retoraran igual
        
        -   si otiginalemte estaban en minusculas 
            permaneceran en maysuculas

"""


cadena1:str = "TEXTO"
cadena2:str = "123124"
cadena3:str = "$%$%((()))"
cadena4:str = "hhhholAAaaa123..."


print(cadena1.capitalize())
print(cadena3.capitalize())
print(cadena2.capitalize())
print(cadena4.capitalize())