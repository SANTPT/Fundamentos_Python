# --- EJEMPLO: GESTIÓN DE COMPRAS Y PRESUPUESTO ---

# 1. Operadores de Asignación (=, +=, -=)
# Empezamos con un presupuesto en nuestra billetera.
presupuesto = 100.0  # Asignación simple
lista_compras = ["Pan", "Leche", "Fruta"]

# 2. Operadores Aritméticos (+, -, *, /, //, %, **)
precio_pan = 1.50
cantidad_pan = 2
subtotal_pan = precio_pan * cantidad_pan  # Multiplicación
presupuesto -= subtotal_pan                # Asignación de resta (presupuesto = presupuesto - subtotal)

total_items = len(lista_compras)
promedio_por_item = presupuesto / total_items  # División decimal

# 3. Operadores de Comparación (==, !=, >, <, >=, <=)
TIENE_DINERO = presupuesto > 50.0  # ¿Nos queda más de la mitad?
ES_CERO = presupuesto == 0.0       # ¿Estamos en quiebra?

# 4. Operadores Lógicos (and, or, not)
tengo_hambre = True
hay_oferta = False

# Decidimos comprar un dulce si: (tengo hambre Y hay presupuesto) O hay una oferta irresistible.
comprar_dulce = (tengo_hambre and presupuesto > 10.0) or hay_oferta
print(f"¿Comprar dulce?: {comprar_dulce}")

# 5. Operadores de Memoria/Pertenencia (in, not in)
# Revisamos si un producto está en nuestra lista de deseos.
producto_buscar = "Chocolate"
esta_en_lista = producto_buscar in lista_compras
no_esta_en_lista = "Pescado" not in lista_compras

print(f"¿Está el {producto_buscar} en la lista?: {esta_en_lista}")

# 6. Operadores de Identidad (is, is not)
# Comparan si dos variables apuntan al MISMO objeto en memoria.
mi_billetera = [presupuesto]  # Una lista con el saldo
billetera_digital = mi_billetera  # Apuntan al mismo objeto
copia_billetera = [presupuesto]     # Es una lista nueva con el mismo valor

print(f"¿Son la misma billetera física?: {mi_billetera is billetera_digital}") # True
print(f"¿Es la copia el mismo objeto real?: {mi_billetera is copia_billetera}")   # False
print(f"¿Pero tienen el mismo valor?: {mi_billetera == copia_billetera}")        # True

# --- RESUMEN FINAL ---
print("\n--- Estado Final del Ejemplo ---")
print(f"Presupuesto restante: ${presupuesto}")
print(f"¿Puedo seguir comprando?: {'Sí' if presupuesto > 0 else 'No'}")
