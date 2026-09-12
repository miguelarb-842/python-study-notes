from validator.vl_letras import vl_text
from utils.analizartext import analizar_text

def main():
    
    texto:str = vl_text("Ingrese la palabra a ser analizada: ")
    analizar_text(texto = texto)
    
if __name__ == "__main__":
    main()