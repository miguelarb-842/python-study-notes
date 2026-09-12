from styles.styles import red_color, blacking
from utils.utils import slepp_enter

def vl_text(mensaje:str = "Ingese un dato")->str:
    
    while True:
    
        valor = input(f"{mensaje}: ")
        valor_normalizado = valor.lower().strip().replace(" ","")
 
        if not valor_normalizado.isalpha():
            
            error:str =f"{blacking(red_color('Error: solo se pueden ingresar letras presione enter para continuar'.upper()))}"
            slepp_enter(error)
            continue
        
        return valor

