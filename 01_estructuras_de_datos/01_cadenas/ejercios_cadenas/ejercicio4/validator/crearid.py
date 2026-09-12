from data.data import usuarios

def crear_id(texto: str):
    cd = len(texto) * 84
    
    if cd > 1000:
        cd += 84
    
    while True:
        
        id_repetido = False
        for usr in usuarios:
            if cd == usr["ID"]:
                cd += 100
                id_repetido = True
                break            
            
        if not id_repetido:
            return cd 
        
