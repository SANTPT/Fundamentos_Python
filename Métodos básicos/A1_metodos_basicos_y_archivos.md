## Python para Principiantes: Métodos Básicos y Archivos

## Introducción
¡Hola! En este documento, vamos a aprender dos cosas muy importantes en Python:

- Cómo tu programa puede **hablar contigo** y recibir tus órdenes.
- Cómo puede **guardar** y **leer** información usando **archivos**.

Usaremos un español muy sencillo para que sea fácil de entender.

## Parte 1: Métodos básicos en Python

### Introducción simple
En Python, los métodos (o funciones) son como **herramientas** que nos ayudan a hacer cosas. Con estos métodos básicos, tu programa puede hablar contigo y tú puedes hablar con tu programa.

### `print()`
`print()` se usa para **mostrar texto o resultados** en la pantalla. Es como si tu programa te dijera algo.

Ejemplo:

```python
print("¡Hola, soy Python!")
print(10 + 5)

nombre = "Ana"
edad = 25
print("Mi nombre es", nombre, "y tengo", edad, "años.")
```

### `type()`
`type()` se usa para ver **qué tipo de dato** es algo. Por ejemplo: texto, número entero, número con decimales, etc.

Ejemplo:

```python
print(type("Hola"))   # str (texto)
print(type(123))      # int (entero)
print(type(3.14))     # float (decimal)
```

### `input()`
`input()` se usa para **recibir información del usuario**. El programa se detiene y espera a que escribas algo y presiones Enter. Lo que escribes se guarda como **texto** (`str`).

Ejemplo:

```python
nombre_usuario = input("¿Cómo te llamas? ")
print("¡Hola,", nombre_usuario, "!")

numero1 = input("Escribe un número: ")
numero2 = input("Escribe otro número: ")

suma = int(numero1) + int(numero2)  # convertimos a entero para sumar
print("La suma es:", suma)
```

### Resumen rápido (Parte 1)
- Con `print()`, tu programa te habla.
- Con `type()`, sabes qué tipo de dato tienes.
- Con `input()`, tú le hablas a tu programa.

## Parte 2: Trabajo y acceso con archivos en Python

### Explicación simple
Trabajar con archivos significa que tu programa puede:

- **Escribir** información en un archivo (guardar).
- **Leer** información de un archivo (recuperar).

Imagina que un archivo es como un cuaderno: puedes escribir notas y leerlas después.

### Tipos de archivos comunes
- **TXT**: texto simple (letras y números).
- **CSV**: tabla de datos separados por comas.
- **JSON**: datos organizados (como diccionarios o listas).

### Métodos importantes
- **`open()`**: abre el archivo indicando el modo (leer o escribir).
- **`with`**: forma segura; cierra el archivo automáticamente.
- **`read()`**: lee el contenido del archivo.
- **`write()`**: escribe contenido en el archivo.

### Ejemplo simple: escribir y leer un `.txt`

```python
from pathlib import Path

ruta_txt = Path(__file__).with_name("mi_archivo.txt")

print("--- Escribiendo en el archivo ---")
with open(ruta_txt, "w", encoding="utf-8") as archivo:
    archivo.write("¡Hola, mundo!\n")
    archivo.write("Estoy aprendiendo Python.\n")

print("\n--- Leyendo del archivo ---")
with open(ruta_txt, "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

print("Contenido del archivo:")
print(contenido)
```

### ¿Qué significan `"w"` y `"r"`?
- **`"w"` (write)**: escribir. Si el archivo no existe, se crea. Si ya existe, se reemplaza.
- **`"r"` (read)**: leer. Lee lo que ya está escrito.

## Conclusión
¡Felicidades! Ya viste cómo interactuar con tu programa usando `print()`, `type()` y `input()`, y también cómo guardar y leer información con archivos. Estas son bases fundamentales para crear programas más útiles e interesantes.

## Archivo de ejemplo (A1)
El ejemplo completo ejecutable está en:
- `Métodos básicos/A1_metodos_basicos_y_archivos.py`

