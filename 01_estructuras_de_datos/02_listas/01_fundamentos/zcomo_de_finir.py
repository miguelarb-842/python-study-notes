"""
    para definir los distintos tipos de listas
    tenemos la fomra 
    
    nombre_lista: list[TIPO_A | TIPO_B] = [elemento1, elemento2]
    
    siendo los tipos los tipos de elementos
    
"""

numeros:list[int] = [5,7,8,10]
nombres:list[str] = ["Miguel","Vanessa","Eduardo","Jose"]
precios:list[float] = [12.32, 3.1416, 78.0, 98.0, 0.99]

persona:list[dict[str: any]] = [
    
    {"nombre":"Miguel","edad":17,"dinero": 12.32},
    {"nombre":"Vanessa","edad":17,"dinero": 9.32},
    {"nombre":"Eduardo", "edad":17, "dinero": 12.32}
        
]