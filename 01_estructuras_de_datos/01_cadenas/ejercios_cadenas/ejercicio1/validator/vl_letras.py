from styles.styles import blacking,green_color,red_color
from utils.utils import slepp_enter

def vl_text(mensaje:str = "Ingese un dato")->str:
    
    while True:
    
        valor = input(f"{mensaje}: ")
        valor_normalizado = valor.lower().strip()

        if not valor_normalizado.isalpha():
            
            error:str =f"{blacking(red_color('Error: solo se pueden ingresar letras presione enter para continuar'.upper()))}"
            slepp_enter(error)
            
            continue
    
        bien:str = f"{blacking(green_color('Todo esta correcto presione enter para continuar'))}"
        slepp_enter(bien)
        return valor
        

vl_text()
