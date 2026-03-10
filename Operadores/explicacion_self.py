class Persona:
    # El método __init__ es el constructor que se ejecuta al crear un objeto.
    # 'self' actúa como un puente que representa al objeto específico que estamos usando.
    def __init__(self, nombre, edad):
        # 'self.nombre' guarda el valor recibido en el 'espacio de memoria' de este objeto.
        # De esta manera, cada persona puede tener su propio nombre.
        self.nombre = nombre
        self.edad = edad

    # Todos los métodos que definamos dentro de una clase deben recibir 'self'.
    def saludar(self):
        # Gracias a 'self', el método sabe qué nombre debe imprimir: el de ESTA persona.
        print(f"Hola, mi nombre es {self.nombre}")

# Ahora creamos un objeto (instancia) de la clase Persona:
# Al pasar "Juan", Python lo recibe como el parámetro 'nombre' y asigna 'persona1' a 'self'.
persona1 = Persona("Juan", 20)

# Al llamar a saludar(), Python envía automáticamente 'persona1' como el argumento 'self'.
persona1.saludar()

