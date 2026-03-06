# # Ejemplo de Indentación de Código y comentario 

# try:
#     edad = int(input("¿Cuántos años tienes? "))
    
#     if edad >= 0:
#         if edad >= 18:
#             print("Ya puedes conducir.")
#         else:
#             print("Aún te faltan unos años para conducir.")
#     else:
#         print("La edad no puede ser negativa.")

# except ValueError:
#     print("Error: Por favor, introduce un número válido.")

'''
Estes codigo  es un ejemplo de 
Documentacion tipo Docstring
'''

#Snake case
# nombre_usuario = "Juan"
# edad_usuario = 25
# Edad_usuario = 35

# def verificar_mayoria_edad(edad):
#     if edad >= 18:
#         print(f"{nombre_usuario} es mayor de edad.")

# verificar_mayoria_edad(edad_usuario)

# #Sensible a mayusculas y minusculas
# print(nombre_usuario)
# print(Edad_usuario)   

# #Declaracion de variables

# # Texto (String) - Usa comillas dobles o simples
# nombre_usuario = "Alex"

# # Números enteros (Integer)
# edad = 28

# # Números con decimales (Float)
# precio_producto = 19.99

# # Valores lógicos (Boolean) - Siempre con Mayúscula inicial
# es_estudiante = True
# tiene_descuento = False

# # Asignar diferentes valores a diferentes variables
# x, y, z = 10, 20, 30

# # Asignar el mismo valor a varias variables
# inicio = fin = contador = 0

# # Declaramos una variable que existe, pero no tiene valor aún
# resultado_examen = None



# print(resultado_examen)

# #f-strings
# nombre = "Elena"
# puntos = 95

# # Directo, limpio y permite operaciones dentro de las llaves
# mensaje = f"Hola {nombre}, tu puntuación es de {puntos} puntos."
# print(mensaje)

# # Ejemplo con operación:
# print(f"El doble de tus puntos es {puntos * 2}")

# #Método .format()
# nombre = "Elena"
# puntos = 95

# # Se usan llaves vacías como "espacios reservados"
# mensaje = "Hola {}, tu puntuación es de {} puntos.".format(nombre, puntos)
# print(mensaje)

# # También puedes usar índices para repetir valores
# repetido = "Usuario: {0}, ¿verdad {0}?".format(nombre)
# print(repetido)

# # Operador %

# nombre = "Elena"
# puntos = 95

# # %s para texto (string), %d para números enteros (decimal/integer)
# mensaje = "Hola %s, tu puntuación es de %d puntos." % (nombre, puntos)
# print(mensaje)


# # Conversión Explícita de string a int
# puntuacion_texto = "100"
# # puntuacion_total = puntuacion_texto + 5  <-- Esto daría ERROR

# puntuacion_int = int(puntuacion_texto)
# puntuacion_total = puntuacion_int + 5    # Ahora sí: 105

# print(puntuacion_total) 

# # Conversión Explícita de int a string
# edad = 25
# mensaje = "Mi edad es " + str(edad)      # Necesario para concatenar con +
# print(mensaje)

# # Conversión Explícita de float a int
# precio = 19.99
# # Conversión explícita
# precio_entero = int(precio)

# print(f"Original: {precio}")        # 19.99
# print(f"Convertido: {precio_entero}") # 19 (Se pierde el .99)

# # Conversión Explícita de int a float
# puntuacion_base = 100

# # Conversión explícita
# puntuacion_decimal = float(puntuacion_base)

# print(puntuacion_decimal)       # Imprime 100.0
# print(type(puntuacion_decimal)) # <class 'float'>

# # Conversión Explícita de string a float
# precio_texto = "25.50"
# precio_float = float(precio_texto)

# print(precio_float)       # Imprime 25.5
# print(type(precio_float)) # <class 'float'> 

# # Conversión Implícita
# numero_entero = 10
# numero_decimal = 5.5

# # Python convierte automáticamente el entero a decimal para sumar
# resultado = numero_entero + numero_decimal

# print(resultado)        # Imprime 15.5
# print(type(resultado))  # <class 'float'>

# # Conversión a Booleano (bool)
# print(bool(0))      # False
# print(bool(42))     # True
# print(bool(""))     # False
# print(bool("Hola")) # True
