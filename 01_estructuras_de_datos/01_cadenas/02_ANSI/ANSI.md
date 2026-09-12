# Codigo de espacios ANSI
    
El nombre viene de que siguen un estándar definido por ANSI 
(American National Standards Institute), originalmente pensado para controlar terminales de texto: mover el cursor, cambiar colores, aplicar negrita, la pantalla, etc.

La estructura es siempre la misma: `\033[código m` \033 (o su equivalente `\x1b`) 
    
### Es el carácter `ESC` (escape):

le dice a la terminal "lo que sigue no es texto normal,es una instrucción" marca el inicio de la secuencia de control.
    
El número (1, 91, 92, etc.) indica qué hacer.
    
### `m` 

Cierra la secuencia (específicamente para códigos de 
formato de texto/color — este tipo se llama SGR, "Select Graphic Rendition").

Por eso 

```py
    RESET = "\033[0m"
```
    
significa literalmente "código 0" = restablecer todo el formato a la normalidad.


### Colores

```py
ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
```

### Estilos de texto

```py
NEGRITA = "\033[1m"
CURSIVA = "\033[3m"
SUBRAYADO = "\033[4m"
```

### Siempre al final de un texto con estilo

```py
RESET = "\033[0m"
```