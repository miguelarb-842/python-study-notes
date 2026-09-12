# Resumen de Métodos de Cadenas en Python

## Búsqueda

### `.find(subcadena, inicio=0, fin=len(str))`
Busca la primera aparición de `subcadena`. Devuelve el **índice** donde empieza, o **-1** si no la encuentra. No lanza error. Sensible a mayúsculas/minúsculas.

```python
"Hola que tal".find("que")   # 5
"Hola que tal".find("xyz")   # -1
```

### `.index(subcadena, inicio=0, fin=len(str))`
Igual que `.find()`, pero si **no** encuentra la subcadena, lanza `ValueError` en vez de devolver -1.

```python
"Hola que tal".index("que")   # 5
"Hola que tal".index("xyz")   # ValueError
```

### `.count(subcadena, inicio=0, fin=len(str))`
Cuenta cuántas veces aparece `subcadena`, sin solapar coincidencias. Si no encuentra ninguna, devuelve `0`.

```python
"la casa de la vaca".count("a")    # 6
"la casa de la vaca".count("la")   # 2
```

### `.startswith(cadena)` / `.endswith(cadena)`
Verifican si el string empieza/termina con `cadena`. Devuelven `True`/`False`. Pueden recibir una **tupla** de opciones.

```python
"documento.pdf".startswith("doc")                      # True
"documento.pdf".endswith((".pdf", ".docx", ".txt"))    # True
```

---

## Transformación (mayúsculas/minúsculas)

### `.lower()` / `.upper()`
Convierten todo el string a minúsculas / mayúsculas.

### `.capitalize()`
Pone en mayúscula solo la **primera letra de todo el string**; el resto queda en minúscula.

```python
"hola que tal".capitalize()   # "Hola que tal"
```

### `.title()`
Pone en mayúscula la primera letra de **cada palabra**.

```python
"hola que tal".title()   # "Hola Que Tal"
```
⚠️ Trata los apóstrofes como separadores de palabra: `"o'brien's".title()` → `"O'Brien'S"`.

---

## Alineación y relleno

### `.center(ancho, caracter_relleno=' ')`
Centra el texto, repartiendo el relleno a ambos lados. Si el ancho es menor o igual al largo del texto, no cambia nada.

### `.ljust(ancho, caracter_relleno=' ')`
Alinea a la **izquierda**; todo el relleno va del lado **derecho**.

### `.rjust(ancho, caracter_relleno=' ')`
Alinea a la **derecha**; todo el relleno va del lado **izquierdo**. Opuesto de `.ljust()`.

### `.zfill(ancho)`
Rellena con **ceros** a la izquierda. A diferencia de `.rjust(ancho, "0")`, respeta el signo `-` dejándolo al frente.

```python
"7".zfill(3)     # "007"
"-7".zfill(4)    # "-007"  (correcto)
"-7".rjust(4, "0")  # "0-07"  (signo mal ubicado)
```

---

## Limpieza de espacios

### `.strip()` / `.lstrip()` / `.rstrip()`
Eliminan espacios en blanco del inicio y/o final. `.strip()` ambos lados, `.lstrip()` solo izquierda, `.rstrip()` solo derecha. También aceptan un carácter específico a eliminar. No afectan espacios en el medio.

```python
"   Hola   ".strip()      # "Hola"
"###Hola###".strip("#")   # "Hola"
```

---

## Reemplazo

### `.replace(viejo, nuevo, cantidad=-1)`
Reemplaza todas las apariciones de `viejo` por `nuevo`. El parámetro `cantidad` (opcional) limita cuántas reemplazar. No modifica el original (los strings son inmutables).

```python
"que tal, que dia".replace("que", "QUE")      # todas
"que tal, que dia".replace("que", "QUE", 1)   # solo la primera
```

---

## División y unión

### `.split(separador=None, maxsplit=-1)`
Divide el string en una **lista**. Sin separador, corta por cualquier espacio en blanco e ignora espacios de más. Con separador específico, corta exactamente ahí (puede generar strings vacíos entre separadores repetidos).

```python
"Hola que tal".split()          # ['Hola', 'que', 'tal']
"a,b,,c".split(",")             # ['a', 'b', '', 'c']
```
---

## Validación de contenido

### `.isalpha()`
`True` si la cadena tiene **solo letras** (sin espacios ni números).

### `.isnumeric()`
`True` si la cadena tiene **solo dígitos**. 
⚠️ `"-5".isnumeric()` → `False` (el signo no es dígito). `"12.5".isnumeric()` → `False` (el punto tampoco).

### `.isalnum()`
`True` si la cadena es letras **y/o** números combinados (sin espacios ni símbolos).

```python
"Hola".isalpha()      # True
"Hola123".isalpha()   # False
"12345".isnumeric()   # True
"Hola123".isalnum()   # True
```

---

## Otros

### `len(objeto)`
**No es un método** (no lleva punto) — es una función incorporada. Cuenta caracteres en un `str`, elementos en una `list`, claves en un `dict`.

```python
len("Hola que tal")   # 12 (incluye espacios)
```

---

## Tabla comparativa rápida

| Método | Qué hace | Devuelve |
|---|---|---|
| `.find()` | busca, no falla | índice o -1 |
| `.index()` | busca, falla si no está | índice o `ValueError` |
| `.count()` | cuenta apariciones | número (0 si no hay) |
| `.replace()` | reemplaza texto | string nuevo |
| `.split()` | string → lista | lista |
| `.join()` | lista → string | string |
| `.strip()` | limpia espacios extremos | string nuevo |
| `.center()/.ljust()/.rjust()` | alinean con relleno | string nuevo |
| `.zfill()` | rellena con ceros (respeta signo) | string nuevo |
| `.isalpha()/.isnumeric()/.isalnum()` | validan contenido | `True`/`False` |

    

.starswith(data)

dada una cada verifica si empieza con esa cadena

.endswith(data)
dada una cada verifica si termina con esa cadena

.count() 

pide un cadana de entrada y cuenta 
las conicidencias
y cuando no se encuentra 
debuelve 0 es decir 0 coincidencias


    METODOS INTEGRADORES EN PY
    
    
    .isnumeric() 
    
        verifica que si es un numero
        auque el numero este declarado como un str el 
        recorre para verificar que lo ingresado 
        sea un numero si dectecta un numero 
        devuelve True en caso contrario devolvera 
        False
        
        Un detalle a tener en cuenta con 
        .isalnum(): acepta letras y 
        números combinados
    
    .isalpha()
    
        verifica que la cadena sea solamente texto y caraceres
        sin algun valor numerico entre si
        al ser alpha osea solo acepta valores 
        de la A-Z sin espacios
        
        ya que los espacios y #"!., 
        son caracter especiales
    
    .zfill() 
    
        — rellena con ceros a 
        la izquierda, útil para IDs o códigos.
    
    
"""


