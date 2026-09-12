from validators.vl_letras import vl_text
from utils.contarvoca import contar_vocales

def main():
    
    texto = vl_text("Ingrese una palabra")
    contar_vocales(texto)

if __name__ == "__main__":
    main()