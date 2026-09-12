def analizar_text(texto:str)->None:
    
    mayus_text = texto.upper()
    minus_text = texto.lower()
    
    normalizar_text = texto.strip().replace(" ", "")
    cantidad_de_letras = len(normalizar_text)
    
    print(f"""
    
    Versiones del texto:
    
    -----------------------
    
    Maysucula = {mayus_text}
    Minuscula = {minus_text}
    
    ------------------------
    
    cantidad de letras en el texto:
    
    {cantidad_de_letras} letras 
    
    -------------------------
          
    """)
    
