from utils.utils import slepp_enter
from styles.styles import red_color,green_color
from data.data import usuarios

def es_usuario_valido() -> str:

    while True: 
        usuario: str = str(input("Ingrese su nombre de usuario: "))
        
        if usuario == "":
            print(red_color("error: no se puede dejar el nombre en blanco ".upper()))
            slepp_enter()
            continue
        
        if " " in usuario:
            print(red_color("error: el nombre de usuario no puede llevar espacios".upper()))
            slepp_enter()
            continue
        
        if len(usuario) < 4 or 12 < len(usuario):
            print(red_color("error: el rango de caracteres del nombre debe de ser mayor a 4 y menor a 12".upper())) 
            slepp_enter()
            continue
        
        if usuario[0].isnumeric():
            print(red_color("error: el usuario no puede empezar con numeros".upper()))
            slepp_enter()
            continue
        
        nombrerep = False
        for usr in usuarios:
            if usuario == usr["nombre"]:
                print(red_color("LO SENTIMOS, ESE NOMBRE YA PERTENECE A UN USUARIO"))
                slepp_enter()
                nombrerep = True
                break
            
        if nombrerep == True:
            continue
        
        print(green_color("El nombre de usuario ha sido exitoso"))
        return usuario
