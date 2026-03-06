"""
Python para Principiantes: Métodos Básicos y Archivos

En este archivo practicamos:
- print(): mostrar mensajes en pantalla
- type(): ver el tipo de dato
- input(): pedir datos al usuario
- Archivos: escribir y leer un .txt
"""

from pathlib import Path


def parte_1_metodos_basicos(presentacion: bool = False) -> None:
    print("=== Parte 1: Métodos básicos (print, type, input) ===\n")

    # print(): mostrar texto, números y variables
    print("Ejemplos de print():")
    print("¡Hola, soy Python!")
    print(10 + 5)

    nombre = "Ana"
    edad = 25
    print("Mi nombre es", nombre, "y tengo", edad, "años.")

    # type(): ver tipos de datos
    print("\nEjemplos de type():")
    print('type("Hola") ->', type("Hola"))
    print("type(123) ->", type(123))
    print("type(3.14) ->", type(3.14))
    print("type(True) ->", type(True))

    # input(): pedir datos al usuario
    print("\nEjemplos de input():")
    nombre_usuario = input("¿Cómo te llamas? ")
    print("¡Hola,", nombre_usuario, "!")

    numero1_texto = input("Escribe un número: ")
    numero2_texto = input("Escribe otro número: ")

    # input() devuelve texto (str), por eso convertimos a int para sumar.
    try:
        suma = int(numero1_texto) + int(numero2_texto)
        print("La suma es:", suma)
    except ValueError:
        print("No pude sumar porque no escribiste números enteros válidos.")


def parte_2_archivos() -> None:
    print("\n=== Parte 2: Archivos (escribir y leer) ===\n")

    # Guardamos el archivo .txt en la misma carpeta que este script,
    # para que funcione aunque lo ejecutes desde otra ruta.
    ruta_txt = Path(__file__).with_name("mi_archivo.txt")

    print("--- Escribiendo en el archivo ---")
    with open(ruta_txt, "w", encoding="utf-8") as archivo:
        archivo.write("¡Hola, mundo!\n")
        archivo.write("Estoy aprendiendo Python.\n")
        archivo.write("Guardar en archivos sirve para no perder información.\n")
    print(f"Texto escrito en: {ruta_txt.name}")

    print("\n--- Leyendo del archivo ---")
    with open(ruta_txt, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
    print("Contenido del archivo:")
    print(contenido)
    print("Lectura terminada.")


def main() -> None:
    print("Python para Principiantes: Métodos Básicos y Archivos\n")
    parte_1_metodos_basicos()
    parte_2_archivos()


if __name__ == "__main__":
    main()

