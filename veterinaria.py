#Creamos la Clase Perro
class Perro:
    nombre = ""
    raza = ""
    edad = 0
    peso = 0
    color = ""
    tamaño = ""
    dueño = ""
    contacto_dueño = ""

#Creamos los metodos
    def __init__(self, nombre, raza, edad, peso, color, tamaño, dueño, contacto_dueño):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.color = color
        self.tamaño = tamaño
        self.dueño = dueño
        self.contacto_dueño = contacto_dueño
        self.estado = "NO ATENDIDO"
        self.cambiar_estado()
        self.definir_tamaño()

    def cambiar_estado(self):
        self.estado = "ATENDIDO"

#en este metodo se evalua si el perro es grande o pequeño
    def definir_tamaño(self):
        if self.peso < 10:
            self.tamaño = "Perro Pequeño"
        else:
            self.tamaño = "Perro Grande"

#con este metodo imprimimos la informacion
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad} años")
        print(f"Peso: {self.peso} kg")
        print(f"Color: {self.color}")
        print(f"Tamaño: {self.tamaño}")
        print(f"Dueño: {self.dueño}")
        print(f"Contacto del Dueño: {self.contacto_dueño}")
        print(f"Estado: {self.estado}")


#pedimos al usuario que registre los datos del perro
nombre = input("Nombre del perro: ")
raza = input("Raza del perro: ")
edad = int(input("Edad del perro: "))
peso = float(input("Peso del perro (kg): "))
color = input("Color del perro: ")
dueño = input("Nombre del dueño: ")
contacto_dueño = input("Contacto del dueño: ")

# Crear objeto perro
perro = Perro(nombre, raza, edad, peso, color, "", dueño, contacto_dueño)

perro.mostrar_informacion()


