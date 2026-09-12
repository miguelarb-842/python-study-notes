def contar_vocales(texto:str)->int:
    
    norm_text = texto.lower()
    
    a:int = norm_text.count("a")
    e:int = norm_text.count("e")
    i:int = norm_text.count("i")
    o:int = norm_text.count("o")
    u:int = norm_text.count("u")
    
    total:int = a + e + i + o + u
    
    print(f"""
          
        la cantidad vocales en el texto es: {total}
          
    """)
    
    return total
    