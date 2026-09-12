from data.data import usuarios
from .crearid import crear_id
from .vl_usr import es_usuario_valido

def crear_usuario():
    
    nombre = es_usuario_valido()
    ID = crear_id(nombre)
    
    print(f"""
          
          Nombre: {nombre}
          ID: {ID}
          """)
    
    usuario_nuevo = {"nombre": nombre, "ID": ID}
    usuarios.append(usuario_nuevo)
    