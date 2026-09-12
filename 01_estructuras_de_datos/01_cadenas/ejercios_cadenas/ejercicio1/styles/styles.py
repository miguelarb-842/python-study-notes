# Colores
ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"

# Estilos de texto
NEGRITA = "\033[1m"
CURSIVA = "\033[3m"
SUBRAYADO = "\033[4m"
TACHADO = "\033[9m"

# Siempre al final de un texto con estilo
RESET = "\033[0m"

def red_color(texto:str)->str:
    return(f"{ROJO}{texto}{RESET}")

def green_color(texto:str):
    return(f"{VERDE}{texto}{RESET}")

def blacking(texto):
    return(f"{VERDE}{texto}{RESET}")


    


    
    
        
    
    
