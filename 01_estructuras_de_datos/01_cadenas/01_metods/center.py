"""


    Es un método de cadenas que 
    centra el texto dentro de un espacio de 
    un ancho determinado, agregando relleno 
    (por defecto espacios) 
    en ambos lados para completar ese ancho.

    cadena:str.center(width,fillchar)
    
    igual que rjust y ljust pero 
    ellos solo ajustan un lado del str

"""

cadena1:str = "TEXTO"
cadena2:str = "123124"
cadena3:str = "$%$%((()))"
cadena4:str = "HolAAaaa123..."

print(cadena1.center(12,"-"))